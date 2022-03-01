import os
import pandas as pd

def find_all(name, path):
    filename_list = []
    for root, dirs, files in os.walk(path):
        if name in files:
            filename_list.append(os.path.join(root, name))
    return filename_list


def extract_results(filename_list):
    All_results = []

    for filename in filename_list:        
        results = {}
        
        model_name = filename.split('/')[-2].split('-')[1]
        type_name = filename.split('/')[-1].split('_')[0]
        print(type_name, model_name)
        
        results["type"] = type_name
        results["model"] = model_name    
        
        with open(filename, 'r') as f:
            train_results = f.readlines()
            for each_line in train_results:
                if "macro-f1" in each_line:
                    results["macro-f1"] = each_line.split("=")[-1].strip()
                elif "micro-f1" in each_line:
                    results["micro-f1"] = each_line.split("=")[-1].strip()
                elif "precision" in each_line:
                    results["precision"] = each_line.split("=")[-1].strip()
                elif "recall" in each_line:
                    results["recall"] = each_line.split("=")[-1].strip()
        
        
        All_results.append(results)

    return All_results

def main():
    path = os.getcwd()
    dev_list = find_all('dev_results.txt', path)
    dev_results = extract_results(dev_list)
    
    test_list = find_all('test_results.txt', path)
    test_results = extract_results(test_list)
    
    df_dev = pd.DataFrame(dev_results)
    df_test = pd.DataFrame(test_results)
    
    df_dev = df_dev[["type", "model", "macro-f1", "micro-f1", "precision", "recall"]]
    df_test = df_test[["type", "model", "macro-f1", "micro-f1", "precision", "recall"]]
    
    sorted_dev_df = df_dev.sort_values(by=['model'], ascending=True)
    sorted_test_df = df_test.sort_values(by=['model'], ascending=True)
    
    # sorted_dev_df.to_csv('dev_results.csv', index = False)
    # sorted_test_df.to_csv('test_results.csv', index = False)
    
    pd.concat([sorted_dev_df, sorted_test_df]).to_csv('all_results.csv', index = False)

if __name__ == '__main__':
    main()

