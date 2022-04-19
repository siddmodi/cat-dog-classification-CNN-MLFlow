# import argparse
# import os
# import shutil
# from tqdm import tqdm
# import logging
# from src.utils.common import read_yaml, create_directories
# import random
# import tensorflow as tf


# STAGE = "TEMPLATE" ## <<< change stage name 

# logging.basicConfig(
#     filename=os.path.join("logs", 'running_logs.log'), 
#     level=logging.INFO, 
#     format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
#     filemode="a"
#     )


# def main(config_path):
#     ## read config files
#     config = read_yaml(config_path)
#     # params = read_yaml(params_path)
#     # pass

#     path_to_model_dir = os.path.join(
#         config["data"]["local_dir"],
#         config["data"]["model_dir"])
    
#     path_to_model = os.path.join(
#         path_to_model_dir, 
#         config["data"]["init_model_file"])


#     early_stopping_cb = tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
#     # ckpt_path = "model_ckpt.h5"
#     ckpt_cb = tf.keras.callbacks.ModelCheckpoint(path_to_model, save_best_only=True)
#     CALLBACKS_LIST = [early_stopping_cb, ckpt_cb]
#     return CALLBACKS_LIST



# if __name__ == '__main__':
#     args = argparse.ArgumentParser()
#     args.add_argument("--config", "-c", default="configs/config.yaml")
#     # args.add_argument("--params", "-p", default="params.yaml")
#     parsed_args = args.parse_args()

#     try:
#         logging.info("\n********************")
#         logging.info(f">>>>> stage {STAGE} started <<<<<")
#         main(config_path=parsed_args.config)#, params_path=parsed_args.params)
#         logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
#     except Exception as e:
#         logging.exception(e)
#         raise e