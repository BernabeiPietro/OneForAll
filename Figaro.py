import os
import codecs
import pandas as pd
import numpy as np

#"primer_lenght= da prendere dall'output fastqc"'

def run_figaro(mp,md):
    os.system(" \
    python3 figaro.py -i "+ mp.output_trimmed+" -o "+mp.path_figaro+" -a "+md["a_l"] +"-f "+md["primer_forward_l"]+ "-r "+md["primer_reverse_l"]+" \
        ")
    figaro_report= mp.path_figaro+"trimParameters.json"
    table=pd.read_json(figaro_report)
    trunc_f=table.trimPosition[0][0]
    trunc_r=table.trimPosition[0][1]
    return trunc_f,trunc_r


#from figaro import figaro
#sequenceFolder=output_fq_qz
#ampliconLength="da chiedere"
#forwardPrimerLength=primer_trim
#reversePrimerLength=primer_trim
#minimumOverlap=20
#resultTable, forwardCurve, reverseCurve = figaro.runAnalysis(sequenceFolder, ampliconLength, forwardPrimerLength, reversePrimerLength, minimumOverlap, fileNamingStandard, trimParameterDownsample, trimParameterPercentile)
