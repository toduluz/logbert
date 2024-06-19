import pandas as pd
import os
import pickle

output_dir = "../output/bgl/"

def deeplog_file_generator(filename, df, features):
    with open(filename, 'w') as f:
        for _, row in df.iterrows():
            for val in zip(*row[features]):
                f.write(','.join([str(v) for v in val]) + ' ')
            f.write('\n')

# Read pkl file as df
train_filepath = output_dir + 'train.pkl'
test_filepath = output_dir + 'test.pkl'

with open(train_filepath, "rb") as f:
    df_train = pickle.load(f)
    df_train = pd.DataFrame(df_train)
with open(test_filepath, "rb") as f:
    df_test = pickle.load(f)
    df_test = pd.DataFrame(df_test)

# Get max label
df_train['Label'] = df_train['Label'].apply(lambda x: max(x))
df_test['Label'] = df_test['Label'].apply(lambda x: max(x))
# Get normal only
train = df_train[df_train['Label'] == 0]
test_normal = df_test[df_test['Label'] == 0]
df_abnormal = df_test[df_test['Label'] == 1]
deeplog_file_generator(os.path.join(output_dir,'train'), train, ["EventId"])
deeplog_file_generator(os.path.join(output_dir, 'test_normal'), test_normal, ["EventId"])
deeplog_file_generator(os.path.join(output_dir,'test_abnormal'), df_abnormal, ["EventId"])


