# 1️⃣ PyTorch Project Template Easy Version

> 원본 템플릿의 리포지토리가 <b>MIT license</b>를 가지고 있기 때문에 저작권상으로 <b>문제가 없음</b>을 밝힙니다.

- AI 프로젝트에 있어 PyTorch를 활용하고자 할 때, 유사한 파일 시스템 구조의 프로젝트들이 많이 보입니다.
- 이러한 구조는 대부분 <b><i><a href="https://github.com/victoresque/pytorch-template">pytorch-template</a></i></b>에서 제공하는 템플릿을 통해 만들어져오고 있습니다.
- 하지만, iPython 기반 <i><b>Jupyter Notebook, Jupyter lab, Google Colab</b></i>과 같은 개발 환경을 사용하다가 주어진 템플릿을 바로 사용하기에는 입문자에게 다소 어려움이 있습니다.
- 이러한 문제점을 해결하고자 해당 리포지토리를 통해 팀원들이 전반적인 흐름을 가져갈 수 있도록 <i><b>PyTorch Project Template Easy Version</b></i>을 제공합니다.
- 원래 템플릿 구조 기반으로 작업이 되었으며, <i><b>File Structure</b></i>에 대한 자세한 설명과 프로젝트를 진행함에 있어 난해함을 초래할 수 있는 부분들을 제거한 <i><b>Easy Version</b></i>을 제공합니다.

# 2️⃣ File Structure

```
Project

```

# 3️⃣ File Description

1. <code>Project</code>: Root Directory

# 4️⃣ Usage
- 

# 5️⃣ Modification

- <code>.flake8</code> 삭제
    - <a href= "https://tech.songyunseop.com/post/2017/05/lint-with-flake8/">flake8 관련 내용</a> -> 코드 컨벤션을 위한 도구
- <code>base/base_model.py</code> 삭제
    - 필요없는 파일이라 판단
- <code>model/model.py</code> 삭제
    - 필요없는 파일이라 판단
- <code>logger</code> 디렉토리 및 하위 폴더 전체 삭제
    - 로그 기록 자체가 필요없다고 판단
- <code>model/loss.py</code>와 <code>model/metric.py</code> 주석
    - 두 파일에 대해서 필요한 부분은 구현을 하면 된다고 주석
    - 굳이 불필요하게 구현을 할 필요는 없다.
- <code>new_project.py</code> 삭제
    <details>
    <summary><code>new_project.py</code></summary>
        <div markdown="1">

    ```python
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
    ```
    </div>
    </details>