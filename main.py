#main.py
import load_vars as lv
#import merge_single as ms
#import merge_master as mm
import program_skeleton as ps
import log as log

"""
The Driver Function for the scraping applicaiton
"""
def main():
    """
    loads the task dictionary, which is a yaml file of config information that is fed to a program skeleton
    """
    task_dictionary = lv.load_config()
    #garbage_log = log.garbage_collector("garbage_log")
    #garbage_log.enable_collection()
    

    #print(dictionary)


    #dictionary['log']['paths_loaded'] = lv.load_paths(dictionary)
    #dictionary['log']['files_loaded'] = lv.load_files(dictionary)
    #dictionary['log']['date_loaded'] = lv.load_date(dictionary)
    #print(dictionary)

    """
    Runs config into the skeleton
    """
    ps.program_skeleton(task_dictionary)
    #print(json_files)
    #log.json_dump(dictionary)
    #log.log(dictionary)

  

if __name__ == "__main__":
    main()