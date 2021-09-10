
import os

if __name__ == '__main__':
    os.system("conda create -n OneForAll -y") #cutadapt
    os.system("conda install -n OneForAll -c bioconda -y cutadapt ")
    os.system("wget https://github.com/picrust/picrust2/archive/v2.4.1.tar.gz")
    os.system("tar xvzf  v2.4.1.tar.gz")
    os.system("conda env update -n OneForAll -f  picrust2-2.4.1/picrust2-env.yaml")  # picrust do

    os.system("wget https://data.qiime2.org/distro/core/qiime2-2021.4-py38-linux-conda.yml")
    os.system("conda env update -n OneForAll -f qiime2-2021.4-py38-linux-conda.yml")  # qiime do
    os.system("rm qiime2-2021.4-py38-linux-conda.yml")

    os.system("git clone https://github.com/Zymo-Research/figaro.git")
    os.system("conda env update -n OneForAll -f figaro/figaro_conda.yml") #figaro do
