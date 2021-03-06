import json
from os import listdir
from anomaly_detection_app.config import project_path


def load_conf(project_name: str) -> str:
    with open(project_path + project_name + "/conf.json") as f:
        conf = json.load(f)

    return conf


def get_crop_config(project_name: str) -> str:
    conf = load_conf(project_name)

    return conf["crop_config"]["crop_parameters"]


def get_mask_config(project_name: str) -> str:
    conf = load_conf(project_name)

    return conf["mask_config"]


def get_camera_config(project_name: str) -> str:
    conf = load_conf(project_name)

    return conf["camera_config"]


def get_threshold_config(project_name: str) -> str:
    conf = load_conf(project_name)

    return conf["threshold_config"]


def get_all_projects() -> dict[str : list[dict[str:str]]]:
    projects = listdir("anomaly_detection_app/projects/")
    project_dict = {"projects": []}
    for p in projects:
        project_dict["projects"].append({"name": p})
    return project_dict


def get_all_image_names(project_name: str) -> dict[str : list[dict[str:str]]]:
    images = listdir(project_path + project_name + "/images/")
    image_names_dict = {"images": [{"name": i} for i in images]}
    return image_names_dict
