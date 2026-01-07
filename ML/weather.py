import pandas as pd
import numpy as np

file_path = "play_tennis_dataset.csv"
df = pd.read_csv(file_path)

df["PlayTennis"] = df["PlayTennis"].str.strip()
df["Outlook"] = df["Outlook"].str.strip()
df["Temperature"] = df["Temperature"].str.strip()
df["Humidity"] = df["Humidity"].str.strip()
df["Wind"] = df["Wind"].str.strip()

df = df.drop(columns=["Day"])  # remove Day column

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_val = 0
    for i in range(len(elements)):
        prob = counts[i] / np.sum(counts)
        entropy_val += -prob * np.log2(prob)
    return entropy_val

def info_gain(data, split_attribute, target_name="PlayTennis"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute] == vals[i]]
        weighted_entropy += (counts[i] / np.sum(counts)) * entropy(subset[target_name])
    return total_entropy - weighted_entropy

def id3(data, features, target_name="PlayTennis"):
    # if all labels are same
    if len(np.unique(data[target_name])) == 1:
        return np.unique(data[target_name])[0]
    
    # if no features left
    if len(features) == 0:
        return data[target_name].mode()[0]
    
    # choose best feature
    gains = [info_gain(data, f, target_name) for f in features]
    best_feature = features[np.argmax(gains)]
    
    tree = {best_feature: {}}
    
    for val in np.unique(data[best_feature]):
        sub_data = data[data[best_feature] == val].drop(columns=[best_feature])
        new_features = [f for f in features if f != best_feature]
        subtree = id3(sub_data, new_features, target_name)
        tree[best_feature][val] = subtree
    
    return tree

features = [col for col in df.columns if col != "PlayTennis"]
decision_tree = id3(df, features)
print("\nDecision Tree:\n", decision_tree)