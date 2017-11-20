import sys

from lib.GithubCodeCollector import GithubCodeCollector
from code_search import code_search
from code_by_repo_search import code_by_repo_search

compiler_path = '...'
kt_code_temp_file = 'code.kt'
log_file = 'log.txt'

github = GithubCodeCollector('...')

no_compile = True if '--no-compile' in sys.argv else False

config = {
    'no_compile': no_compile,
    'compiler_path': compiler_path,
    'kt_code_temp_file': kt_code_temp_file,
    'log_file': log_file
}

# code_search(github, config)
code_by_repo_search(github, config)