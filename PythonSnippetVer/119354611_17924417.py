from fabric.api import *
env.hosts = ['123.456.789.101']
env.user = 'John'
env.key_filename = '/Users/John/.ssh/google_compute_engine'
env.forward_agent = True
def update():
  '''
  update workers code
  '''
  with cd('~/myrepo'):
      # pull changes
      print colors.cyan('Pulling changes...')
      run('git pull origin master')