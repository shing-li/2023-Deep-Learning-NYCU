# HW1 
### 台語語音辨認（Speaker-dependent）using ESPnet Toolkit  
[ESPnet: end-to-end speech processing toolkit](https://github.com/espnet/espnet)

[kaggle連結](https://www.kaggle.com/competitions/espnet-taiwanese-asr1/overview)

```Python
先安裝anaconda
conda create --name espnet python=3. # 虛擬環境
conda activate espnet
git clone https://github.com/espnet/
cd espnet/tools
CONDA_TOOLS_DIR=$(dirname ${CONDA_EXE})/..
./setup_anaconda.sh ${CONDA_TOOLS_DIR} espnet 3.9
make
cd espnet/tools
make kenlm.done

# 換成自己的data
ls local/data.sh
data_url=
註解建資料的指令
註解移除空白的指令 paste data/${x}/text  

# 修改model大小：batch_bins
cd conf/ 
train_asr_branchformer.yaml
train_lm_transformer.yaml

cd espnet/egs2/aishell/asr1/
# ngpu: gpu數量、stage: 從中斷的地方繼續
./run.sh --ngpu 2 --stage N 

```

