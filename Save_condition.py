import os
import json

def save_cond_md(md,mp):
    p = mp.path_base
    file_name = "config_file.txt"
    cn = os.path.join(p,file_name)
    with open(cn, 'w') as file:
        file.write(json.dumps(md, indent=10))

#da fare un file apposta per far leggere li impostazioni da file
#def read_cond_md(md)# use `json.loads` to do the reverse
  #  json.loads(md["cond_file"])