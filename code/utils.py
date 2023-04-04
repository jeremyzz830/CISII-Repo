import numpy as np
import h5py
import subprocess

def get_3d_landmarks(source_file_path :str, source_file_type:str, label_idx:int=11) -> dict:
    '''
    get 3d landmarks from a file with specified suffix
    and return a numpy array
    
    Params:
    -------
    source_file_path: str
        path to the file
    source_file_type: str
        suffix of the file, could be 'fcsv', 'txt', 'csv'
    label_idx: int
        the index of the tag "label" in the fcsv file, 
        this can be found on the third line of the fcsv file
        it corresponds to the index of the landmarks name in the fcsv file
    
    Returns:
    --------
    a dictionary with keys: 'landmarks_name', 'landmarks_info'
    '''

    if source_file_type == 'fcsv':
        # read the fcsv file
        landmarks = {} # a dictionary to store all the information of the landmarks
        header = [] # a list to store the header of the fcsv file
        with open(source_file_path, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            if line[0] == '#':
                header.append(line)
            else:
                # get the landmarks name
                landmarks_name = line.split(',')[label_idx]
                # get the landmarks info
                landmarks_param = line.split(',')[1:11]
                # landmarks_param = np.asarray(landmarks_param, dtype=np.float32)
                # print(landmarks_name)
                # print(landmarks_param)
                landmarks[landmarks_name] = landmarks_param 
        # get the landmarks name
        landmarks['header'] = header
    
    elif source_file_type == 'txt':
        pass # TODO
    elif source_file_type == 'csv':
        pass # TODO

    return landmarks
    

def write_3d_landmarks_xreg(output_file_path:str, landmark_info:dict):
    '''
    write the 3d landmarks to a file with specified suffix
    '''
    output_fcsv_header = ''
    output_fcsv_value = ''

    for key in landmark_info.keys():
        if key == 'header':
            for header in landmark_info['header']: output_fcsv_header += header

        else:
            # if the landmark's name is in lower case, convert it to upper case
            label = regulate_landmark_label(key)

            # put the landmarks info into a string
            # ','.join() is used to convert a list to a string with ',' as the separator
            output_fcsv_value += ',' + ','.join(landmark_info[key]) + ',' + label +', , \n'

    with open(output_file_path,'w') as f:
        f.write(output_fcsv_header)
        f.write(output_fcsv_value)

    f.close()

def regulate_landmark_label(src_label_name:str, src_label_template:str='r_sps', target_label_template:str='SPS-r') -> str:
    '''
    rename the label name of the landmarks based on the source label template and the target label template

    Params:
    -------
    src_label_name: str
        the name of the source label
    src_label_template: str
        the template of the source label, e.g. 'r_sps', 'l_sps', l stands for left, r stands for right, sps stands for sacroiliac point
    target_label_template: str
        the template of the target label, e.g. 'SPS-r', 'SPS-l'
    
    Returns:
    --------
    target_label_name: str
        the name of the target label after regulation
    '''
    if src_label_template[1] == '_': 
        anatomy_name = src_label_name.split("_")
        target_label_name =  ''.join(anatomy_name[1:-2:-1]).upper() + '-' + ''.join(anatomy_name[0])
        print(target_label_name)

    elif src_label_template[1] == '-': 
        # anatomy_name = src_label_name.split("-")
        pass # TODO

    return target_label_name

def run_xreg(runOptions: str):
    '''Call the executable file
    Params:
    -------
    runOptions: str
        'run_reg' or 'run_viz' , 
        'run_reg' is used to run the registration
        'run_viz' is used to visualize the registration result

    Returns:
    --------
        None 
      
    '''

    if runOptions == 'run_reg':
        print("run_reg is running ...")

        result = subprocess.run([   "bin/xreg-hip-surg-pelvis-single-view-regi-2d-3d",
                                    "data/pelvis.nii.gz",
                                    "data/pelvis_regi_2d_3d_lands_wo_id.fcsv",
                                    "data/example1_1_pd_003.h5",
                                    "result/regi_pose_example1_1_pd_003_proj0.h5",
                                    "result/regi_debug_example1_1_pd_003_proj0_w_seg.h5",
                                    "-s",
                                    "data/pelvis_seg.nii.gz"], stdout=subprocess.PIPE)

        # Print the output of the executable file
        print(result.stdout.decode())

    elif runOptions == 'run_viz':
        result = subprocess.run([   "bin/xreg-regi2d3d-replay",
                                    "result/regi_debug_example1_1_pd_003_proj0_w_seg.h5",
                                    "--video-fps",
                                    "10",
                                    "--proj-ds",
                                    "0.5"], stdout=subprocess.PIPE)
        print(result.stdout.decode())

def readh5(h5_path: str):
    '''Read the h5 file
    Params:
    -------
    h5_path: str
        path to the h5 file

    Returns:
    --------
        None 
      
    '''
    with h5py.File(h5_path, 'r') as f:
        # List all groups
        print("Keys: %s" % f.keys())

        key_list = list(f.keys())

        print(key_list[1])
        data = f['proj-001']
        # data = [0,1]

        print()

    return data

if __name__=='__main__':
    # source_file_path = 'data/case-100114/landmarks.fcsv'
    # source_file_type = 'fcsv'
    # lm_3d = get_3d_landmarks(source_file_path, source_file_type)
    # # print(lm_3d)
    # write_3d_landmarks_xreg('data/test.fcsv', lm_3d)

    data = readh5('data/example1_1_pd_003.h5')
    