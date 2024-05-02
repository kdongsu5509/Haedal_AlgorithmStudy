from collections import Counter
from datetime import datetime
import os
import re

# 각자 해결한 문제의 개수와 제출한 파일의 개수를 세어서 리스트로 반환하는 함수입니다.
def count_problem_source_code(): 
    #6명의 정보를 저장할 2차원 배열입니다.
    ps_code_list = [[] for _ in range(6)]

    # 현재 디렉토리에 있는 디렉토리 리스트를 가져온다.
    directory_list = ['DSKO', 'MSKIM', 'HHNAM', 'JMRYU', 'CSLEE', 'SYCHOI']

    idx = 0
    for x in range(len(directory_list)): # 현재 디렉토리에 있는 디렉토리 리스트를 하나씩 가져온다. _ 구분은 이름으로 한다.
        directory = directory_list[x]
        code_list = os.listdir(f"./{directory}")
        code_list = [name for name in code_list if "Hello" not in name and re.match(r'\d+\.', name)]
        
        #확장자 삭제 전 언어별 통계 정보를 저장할 변수를 선언합니다.
        python_cnt = code_list.count('.py')
        java_cnt = code_list.count('.java')
        csharp_cnt = code_list.count('.cs')
        c_cnt = code_list.count('.c')
        cpp_cnt = code_list.count('.cpp')

        code_list = [name.replace('.py', "").replace('.java', "").replace('.cs', "").replace('.c', "").replace('.cpp', "") for name in code_list if name.endswith(".py") or name.endswith(".java") or name.endswith(".cs") or name.endswith(".c") or name.endswith(".cpp")]

        ps_code_list[idx] += code_list
        idx+=1

        # 각 학생별로 제출한 코드의 개수를 저장할 리스트입니다.
        code_cnt_info = []
        total_code_cnt = []
        language_cnt = []

        


        for i in range(6):
            code_cnt_info.append(len(ps_code_list[i]))
            temp_set = set(ps_code_list[i])
            total_code_cnt.append(len(temp_set))
            language_cnt.append([python_cnt, java_cnt, c_cnt, cpp_cnt, csharp_cnt])

    return code_cnt_info, total_code_cnt, language_cnt

# README.md 파일을 업데이트하는 함수입니다.
def make_read_me(code_cnt_info, total_code_num, language_cnt):
    name_list = ['고동수', '김민승', '남현호', '류정민', '이창석', '최수연']
    base1 = f"""## 📚2024-1 해달 알고리즘 스터디!📚
- 2024년 7월 31일까지 100문제를 모두 해결하는 것을 목표로 합니다.
- 7월 31일에 못 푼 문제 1개당 1,000원의 벌금이 있습니다.
- 벌금은 책걸이 행사 때 사용됩니다.
<br><br><br>

## 참여자 별 현황 한 눈에 보기
<table>
    <th>   이름   </th>
    <th>   총 해결한 문제 수   </th>
    <th>   총 작성한 코드 수   </th>
    <th>   남은 개수  </th>
    <th>   언어별 통계   </th>
"""
    

    table_info = f""
    for i in range(6):
        table_info += f"""  <tr>
        <td> {name_list[i]} </td>
        <td> {total_code_num[i]} </td>
        <td> {code_cnt_info[i]} </td>
        <td> {100 - total_code_num[i]} </td>
        <td> Python : {language_cnt[i][0]} Java : {language_cnt[i][1]} C : {language_cnt[i][2]} <br> C++ : {language_cnt[i][3]} C# : {language_cnt[i][4]}</td>
    </tr>"""
        
    base2 = f"""</table>

# 업로드 방법
### 1. 파일명
- 파일명은 "문제 번호(책 기준) + 확장자"입니다.
- 예시 : 72.py, 14.java , 8.cs

### 2. 깃허브 업로드
- 본인의 이름 폴더에 업로드 해주시면 됩니다!
- `git bash` 명령어는 다음과 같은 순서대로 입력해주세요.
-     `git pull` // 깃허브에 있는 파일을 본인 컴퓨터로 가져옵니다.
-     `git add .` // 본인 컴퓨터에 있는 파일을 로컬 Git에 업로드 합니다.
-     `git commit -m "message"` //메세지를 추가하여 커밋합니다.
-     `git push` // 깃허브에 업로드 합니다
- 위의 방법대로 업로드 하지 않을 경우 README.md가 정상 업데이트 되지 않으니 다들 부탁드려요~


# 최초 사용
- 본인의 컴퓨터에서 "Git Bash"를 실행합니다.
- `git clone "https://github.com/kdongsu5509/Haedal_AlgorithmStudy.git"`을 입력하여 저장소를 복제합니다.
- 복제가 완료되면 본인의 이름으로 된 폴더를 찾아 들어갑니다.
- 본인의 이름으로 된 폴더 안에 자신의 코드를 업로드 합니다.
- 업로드가 완료되면 `git add .` -> `git commit -m "message"` -> `git push`를 통해 업로드 합니다.
- *업로드가 완료되면 자동으로 해당 주차의 README.md 파일을 업데이트 됩니다.*
"""

    return base1 + table_info + base2

# README.md 파일을 업데이트하는 함수입니다.
def update_readme_md():
    code_cnt_info, total_code_num, language_cnt = count_problem_source_code() #반환은 list로 받는다.

    readme = make_read_me(code_cnt_info, total_code_num, language_cnt)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
       f.write(readme)
