class Simple_git:
    def __init__(self):
        self.main = Node("main", 0)
        self.head = self.main
        self.history = []

    def checkout(self, branch_name):
        assert self.head.prev != None, "There is no tracked file."
        assert isinstance(branch_name, str)
        assert hasattr(self, branch_name), f"[{branch_name}] branch does not exist"
        self.head = getattr(self, f"{branch_name}") #입력받은 branch name을 찾아서 해당 branch를 self.head로 지정해준다.
        print(f"[Head] points to [{branch_name}] now") #Head가 변경되었음을 알린다.
        
    def commit(self, file):
        assert isinstance(file, File)
        if self.head.prev != None:
            if self.head.prev.data.content == file.content:
                self.status(file)
                print("Nothing will be committed.")
                return
        
            else: #현재 Head의 전 node 값이 none이 아닐때, (해당 head의 전 node를 밀어내야하므로 구별하였다.)
                version = f"{self.head.name} v{self.head.data + 1}" #branch node 이름 지정
                v_node = Node(version, file) #version node 생성
                c_node = self.head #현재 head의 위치를 저장해준다.
                v_node.prev = deepcopy(self.head.prev) #version node의 전 node에 현재 head의 전 node를 deepcopy 해준다.
                self.head.prev = deepcopy(v_node) #현재 head의 전 node에 생성해준 version node를 deepcopy 해준다.
                self.head.data += 1 #해당 브랜치 노드의 노드 개수가 하나 증가하였으므로, 노드의 개수, 즉 self.head.data에 1을 더해준다.
                
        else: #현재 Head의 전 node가 존재하지 않을 때 (값이 none일때)
            version = f"{self.head.name} v{self.head.data + 1}" #branch node
            v_node = Node(version, file) #version node 생성
            self.head.data += 1 
            self.head.prev = deepcopy(v_node) #해당 head 의 prev 값이 없으므로 전 노드들을 밀어낼 필요 없이 바로 version node를 head.prev에 deepcopy 해준다.
            
        
        if self.head.prev.prev == None:
            self.history.append(
                f"On branch [{self.head.name}], Changes are committed.\n"
                f"The version is {version}\n\n"
                f"(Nothing was committed)\n(=>)\n{self.head.prev.data.content}\n"
            )
        else:
            self.history.append(
                f"On branch [{self.head.name}], Changes are committed.\n"
                f"The version is {version}\n\n"
                f"{self.head.prev.prev.data.content}\n(=>)\n{self.head.prev.data.content}\n"
            )

    def branch(self, branch_name):
        assert self.head.prev != None, "There is no tracked file."
        assert isinstance(branch_name, str)
        a = Node(branch_name, 0) #변수에 새로운 branch node를 생성하여 저장해준다.
        setattr(self, f"{branch_name}", deepcopy(a)) #만들어준 branch node를 self.(branch 이름) 에 deepcopy 해준다.
        getattr(self, f"{branch_name}").prev = deepcopy(self.head.prev) #생성된 브랜치 노드는 사용 중인 브랜치 노드가 가리키고 있는 버전 노드를 가리키게 한다. 이때 사용 중인 브랜치 노드는 변하지 않음.

    def reset(self):
        assert self.head.prev != None, "There is no tracked file."
        assert self.head.data != 0, f"This branch doesn't contain a commit."
        self.head.data -= 1 #version node를 하나 삭제하기 때문에 branch node의 data 값을 하나 감소시킨다.
        self.head.prev = deepcopy(self.head.prev.prev) #version node를 하나 제거했으므로, head.prev에 head.prev.prev를 deepcopy하는 식으로 data를 밀어준다.
        
        self.history.append(
                f"On branch [{self.head.name}], The last commit was reset.\n"
                f"{f'The version is {self.head.name} v{self.head.data}' if self.head.data != 0 else 'Nothing was committed'}\n"
                + "-" * 30
            )


    def merge(self, src_branch, dst_branch):
        assert self.head.prev != None, "There is no tracked file."
        assert isinstance(src_branch, str)
        assert isinstance(dst_branch, str)
        
        src_branch = getattr(self, src_branch)
        dst_branch = getattr(self, dst_branch)

        assert (
            src_branch != self.main
        ), f"[main] branch can not be merged into another branch."
        
        self.head = dst_branch #두 branch를 merge 할때, head는 dst_branch로 이동해준다.
        new_file = File("new", deepcopy(dst_branch.prev.data.content) + "\n" + deepcopy(src_branch.prev.data.content)) #입력받은 두 branch의 data.content를 합쳐 새로운 File 을 만든다.
        self.history.append("merged\n" + "-" * 30) #두 branch가 merge 됐다고 알림
        self.commit(new_file) #새롭게 만든 File 을 commit해줌으로서 두 branch를 merge 시킨다..
        
        
    def log(self):
        assert self.head.prev != None, "There is no tracked file."

        for i in self.history:
            print(i)
            print("-" * 30)

        print(f"(Head -> {self.head.name})")

    def status(self, file):
        assert isinstance(file, File)
        assert self.head.prev != None, "There is no tracked file."
        if self.head.prev.data.content == file.content:
            print("Nothing has changed!") #version node와 입력받은 file의 내용이 다르지 않을 경우 바뀐것이 없다고 출력.
        else:
            print(f"There are {file.name}'s changes to be committed!") #다를 경우, 해당 file에 commit 할 변경 사항이 존재한다고 알림.
        
    def get_file(self, branch_name, version):
        assert self.head.prev != None, "There is no tracked file."
        assert isinstance(branch_name, str)
        assert isinstance(version, int)
        
        self.checkout(branch_name)
        assert version <= self.head.data, f"The latest version is {self.head.prev.name}"
        
        version = f"{branch_name} v{version}"
        
        temp_head = self.head
        while temp_head is not None:
            found = False #입력받은 version의 node를 찾은 여부를 확인하는 변수 생성
            prev = None #해당 branch의 모든 version과 입력받은 version을 비교하기 위해 생성한 변수. 이는 현재 temp_head와 version이 일치하지 않는 경우 temp_head의 값을 prev에 저장하는 방식이다.
            while not found: #찾으려는 version을 찾지 못한 경우
                if temp_head.name == version: #temp_head의 이름과 version의 이름이 같을 경우 found 를 True 로 변경하여 while문 탈출
                    found = True
                else: #temp_head의 이름과 version의 이름이 같지 않을 경우, 현재의 temp_head를 prev 변수에 저장한 뒤, temp_head의 이전 노드를 temp_head에 저장하여 계속 비교.
                    prev = temp_head
                    temp_head = temp_head.prev
            return "-" * 30 + f"\nThis version is {version}\n\n" + str(temp_head.data) #해당 version의 data 출력.

        assert False, "Please check the version!"
