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
        code_list = os.listdir(f".{directory}")
        code_list = [name.replace('.py', "").replace('.java', "").replace('.cs', "") for name in code_list if name.endswith(".py") or name.endswith(".java") or name.endswith(".cs")]

        ps_code_list[idx] += code_list
        idx+=1

        # 각 학생별로 제출한 코드의 개수를 저장할 리스트입니다.
        code_cnt_info = []
        for i in range(6):
            code_cnt_info.append(len(ps_code_list[i]))

        total_code_cnt = []
        for i in range(6):
            temp_set = set(ps_code_list[i])
            total_code_cnt.append(len(temp_set))
    return code_cnt_info, total_code_cnt


# README.md 파일을 업데이트할 때 사용할 문구를 만드는 함수입니다.
def make_count_info(total_code_num, code_cnt_info):
    name_list = ['고동수', '김민승', '남현호', '류정민', '이창석', '최수연']

    info_list = [] # 각 학생별 정보를 저장할 리스트입니다.
    for i in range(6):
        temp_str = f"{name_list[i]}님{code_cnt_info[i]}개"
    count_info = f"#### {name}님이 현재까지 해결한 총 문제 수 : {total_code_num}개\n"
    code_info = f"#### {name}님이 현재까지 작성한 총 코드 수 : {total_code_num}개\n"

    for name in code_cnt_info:
        temp = f"- {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info

# README.md 파일을 업데이트하는 함수입니다.
def make_read_me(code_cnt_info, total_code_num):
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
"""
    

    table_info = f""
    for i in range(6):
        table_info += f"""  <tr>
        <td> {name_list[i]} </td>
        <td> {code_cnt_info[i]} </td>
        <td> {total_code_num[i]} </td>
        <td> {100 - code_cnt_info[i]} </td>
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
- 위의 방법대로 업로드 하지 않을 경우 README.md가 정상 업데이트 되지 않으니 다들 부탁드려요~"""

    return base1 + table_info + base2

# README.md 파일을 업데이트하는 함수입니다.
def update_readme_md():
    code_cnt_info, total_code_num = count_problem_source_code() #반환은 list로 받는다.

    readme = make_read_me(code_cnt_info, total_code_num)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
       f.write(readme)
