"""
Task Queue
medium
TaskQueue（タスクキュー）というシンプルなスケジューラアプリを作成しましょう。TaskQueue はタスクを格納し、それらを順番に（FIFO - First In First Out 方式）処理するキューです。

実装するクラスと機能：
- Item クラス：
    callable data：ラムダ関数としての要素の値
    Item next：次のノードを指し示すプロパティ。デフォルトは null。
- Queue クラス：
    Item head：キューの先頭を指し示すプロパティ。デフォルトは null。
    Item tail：キューの末尾を指し示すプロパティ。デフォルトは null。
    callable peekFront()：キューの先頭のアイテムの値（ラムダ関数）を返すメソッド。
    void enqueue(callable data)：キューの末尾にアイテムを追加するメソッド。
    callable dequeue()：キューの先頭のアイテムを取り除き、その値（ラムダ関数）を返すメソッド。
- TaskQueue クラス：
    Queue queue：Queue クラスのインスタンス。
    void push(callable task)：キューの末尾にタスク（ラムダ関数）を追加するメソッド。
    boolean taskExist()：キュー内にタスクが存在するかどうかを判断するメソッド。
    void run()：キューの先頭のタスクを実行するメソッド。
TaskQueue クラスの push() メソッドによって TaskQueue に挿入される各タスクは、以下のラムダ関数です。
    void firstTask()：文字列 "Running the first function!!!" を出力するラムダ関数。
    void secondTask()：文字列 "Running the second function~~~" を出力するラムダ関数。
    void thirdTask()：文字列 "Running the third function>>>" を出力するラムダ関数。
    void fourthTask()：文字列 "Running the fourth function<<<" を出力するラムダ関数。

テストケース

scheduler = new TaskQueue()
scheduler.push(firstTask)
scheduler.push(secondTask)
scheduler.push(thirdTask)
scheduler.push(fourthTask)

while(scheduler.taskExists()) scheduler.run()
--> Running the first function!!!
--> RRunning the second function~~~
--> RRunning the third function>>>
--> RRunning the fourth function<<<
"""

class Item:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek_front(self):
        if self.head is None:
            return None
        return self.head.data

    def enqueue(self, func):
        if self.head is None:
            self.head = Item(func)
        elif self.tail is None:
            self.tail = Item(func)
            self.head.next = self.tail
        else:
            self.tail.next = Item(func)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        elif self.tail is None:
            temp = self.head
            self.head = None
            return temp.data
        else:
            temp = self.head
            self.head = self.head.next
            if self.head == self.tail:
                self.tail = None
            return temp.data

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, func):
        self.queue.enqueue(func)

    def task_exists(self):
        return self.queue.peek_front() is not None

    def run(self):
        if self.task_exists():
            print(self.queue.dequeue()())

if __name__ == "__main__":
    first_task = lambda: "Running the first function!!!"
    second_task = lambda: "Running the second function~~~"
    third_task = lambda: "Running the third function>>>"
    fourth_task = lambda: "Running the fourth function<<<"

    scheduler = TaskQueue()
    scheduler.push(first_task)
    scheduler.push(second_task)
    scheduler.push(third_task)
    scheduler.push(fourth_task)

    while scheduler.task_exists():
        scheduler.run()

    #--> Running the first function!!!
    #--> RRunning the second function~~~
    #--> RRunning the third function>>>
    #--> RRunning the fourth function<<<
