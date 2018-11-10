```{python}
import gzip

def save_policies(self, policies_file_name):
    policies_str = json.dumps(obj=self.policies, indent=4)
    policies_bytes = policies_str.encode(encoding='utf-8')
    with gzip.GzipFile(filename=policies_file_name, mode='w') as save_file:
        save_file.write(policies_bytes)
    # with open(file=policies_file_name, mode='w') as save_file:
    #     json.dump(obj=self.policies, fp=save_file, indent=4)

def load_policies(self, policies_file_name):
    with gzip.GzipFile(filename=policies_file_name, mode='r') as read_file:
        policies_bytes = read_file.read()
    policies_json = policies_bytes.decode(encoding='utf-8')
    policies = json.loads(policies_json)
    # with open(file=policies_file_name, mode='r') as read_file:
    #     self.policies = json.load(fp=read_file)
```
