class element:
    # 생성자
    def __init__(self, value, link):
        self.value = value
        self.link = link


class queue:
    # 생성자
    def __init__(self):
        self.rear = None
        self.front = self.rear

    # 데이터 삽입 - rear 에 데이터를 붙인다.
    def enqueue(self, value):
        if self.rear is None and self.front is None:
            elem = element(value, None)
            self.rear = elem
            self.front = elem
        else:
            elem = element(value, None)
            self.rear.link = elem
            self.rear = elem

    # 데이터 출력 - front 에서 데이터를 꺼낸다.
    def dequeue(self):
        if self.front is None:
            return None
        else:
            elem = self.front
            self.front = self.front.link
            return elem.value

    # todo: 데이터 순서 뒤집기
    def reverse(self):
        curr = self.front
        prev = None
        while curr is not None:
            nxt = curr.link
            curr.link = prev
            prev = curr
            curr = nxt
        self.rear, self.front = self.front, self.rear

q = queue()  # queue 에 대한 인스턴스 생성
for i in range(10):
    q.enqueue(i)

q.reverse()

for i in range(10):
    print(q.dequeue())
