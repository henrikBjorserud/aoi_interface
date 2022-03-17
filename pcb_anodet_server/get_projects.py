import json


def load_conf(project_name):

    with open('projects/' + project_name + '/conf.json') as f:
        conf = json.load(f)

    return conf


def get_crop_config(project_name):
    conf = load_conf(project_name)

    return conf["crop_config"]["crop_parameters"]


def get_mask_config(project_name):
    conf = load_conf(project_name)

    return conf["mask_config"]


def get_path_config(project_name):
    conf = load_conf(project_name)

    return conf["path_config"]["path"] + project_name


def get_camera_config(project_name):
    conf = load_conf(project_name)
    
    return conf["camera_config"]


def get_threshold_config(project_name):
    conf = load_conf(project_name)

    return conf["threshold"]