import os
import sys

# if running in lambda
if 'LAMBDA_TASK_ROOT' in os.environ:
  sys.path.append(f"{os.environ['LAMBDA_TASK_ROOT']}/lib")

# this will render all of your packages placed as subdirs available
sys.path.append(os.path.dirname(os.path.realpath(__file__)))