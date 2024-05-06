import transformers


MAX_LEN = 128
TRAIN_BATCH_SIZE = 16
VALID_BATCH_SIZE = 3
EPOCHS = 8
BERT_PATH = "google-bert/bert-base-multilingual-cased"
MODEL_PATH = "model.bin"
TRAINING_FILE_1 = "dataset/v_d.csv"
TRAINING_FILE_2 = "dataset/s_d.csv"
TRAINING_FILE_3 = "dataset/e_d.csv"
files = []
files.append(TRAINING_FILE_1)
files.append(TRAINING_FILE_2)
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)