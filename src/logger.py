import json
import time

def log_run(run_name, metrics, filepath='runs.json'):
    entry = {'run': run_name, 'timestamp': time.time(), 'metrics': metrics}
    with open(filepath, 'a') as f:
        f.write(json.dumps(entry) + '\n')
