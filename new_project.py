import sys
from pathlib import Path
from shutil import copytree, ignore_patterns

# 현재 프로젝트를 복제하기 위함이다. -> 필요 없다고 판단.

# This script initializes new pytorch project with the template files.
# Run `python3 new_project.py ../MyNewProject` then new project named 
# MyNewProject will be made

# 현재 디렉토리 == os.getcwd()
current_dir = Path() 
# 이 디렉토리가 파일 형태여야 한다. -> 이게 무슨 의미를 갖는지는 모르겠다.
# 없어도 오류가 난다. -> 아마 있어야 한다는 의미일 거 같다.
assert (current_dir / 'new_project.py').is_file(), 'Script should be executed in the pytorch-template directory'
# 프로젝트 이름이 있어야 한다.
assert len(sys.argv) == 2, 'Specify a name for the new project. Example: python3 new_project.py MyNewProject'

project_name = Path(sys.argv[1])
target_dir = current_dir / project_name

ignore = [".git", "data", "saved", "new_project.py", "LICENSE", ".flake8", "README.md", "__pycache__"]
# 폴더를 통째로 복사한다.
copytree(current_dir, target_dir, ignore=ignore_patterns(*ignore))
print('New project initialized at', target_dir.absolute().resolve())