"""
Event Queue
medium
問題 453 では、TaskQueue というシンプルなスケジューラアプリを作成しました。この問題では、EventQueue というイベント管理システムを作成することが目標です。EventQueue は、イベント名とそれに対応するコールバック（ラムダ関数）を管理するためのデータ構造です。各イベントはハッシュマップとして表現され、イベント名をキーに、そのイベントに対応するコールバックをキューで管理します。

キューは、イベントやタスクを追加された順序で処理するために重要です。キューは FIFO の原則に基づき、最初に追加された要素を最初に取り出します。これにより、イベントが登録された順序でコールバックを実行することが可能になります。また、キューの操作は効率的であり、追加（enqueue）や取り出し（dequeue）を O(1) で行うことができます。

必要なクラスとその機能：
- Item クラス：
    callable data：ラムダ関数としての要素の値
    Item next：次のノードを指し示すプロパティ。デフォルトは null。
- Queue クラス：
    Item head：キューの先頭を指し示すプロパティ。デフォルトは null。
    Item tail：キューの末尾を指し示すプロパティ。デフォルトは null。
    callable peekFront()：キューの先頭のアイテムの値（ラムダ関数）を返すメソッド。
    void enqueue(callable data)：キューの末尾にアイテムを追加するメソッド。
    callable dequeue()：キューの先頭のアイテムを取り除き、その値（ラムダ関数）を返すメソッド。
- EventQueue クラス：
    array queue：イベント名をキーとし、そのイベントに対応する Queue オブジェクトを値とするハッシュマップ（連想配列）を使用します。
    void push(string $event, callable $lambda)：特定のイベント名に対応するキューに新しいラムダ関数を追加するメソッド。イベント名がハッシュマップに存在しない場合、新しいキューを作成して追加します。
    boolean eventExists(string event)：指定したイベント名のキューがハッシュマップに存在し、空でないことを確認するメソッド。
    void dispatch(string event)：特定のイベント名に対応するキューからラムダ関数を取り出し、実行します。対応するイベントがない場合は、"Event is none!" と表示します。

- EventQueue に挿入されるラムダ関数の例：
    void math()："You will study math today" を出力するラムダ関数。
    void music()："You will study music today" を出力するラムダ関数。
    void squat()："You will work out squat 6 times today" を出力するラムダ関数。
    void pushUp()："You will work out squat 20 Push-up today" を出力するラムダ関数。

テストケース
myEventQueueSystem = new EventQueue()
myEventQueueSystem.push("Study", math)
myEventQueueSystem.push("Study", music)
myEventQueueSystem.push("WorkOut", squat)
myEventQueueSystem.push("WorkOut", pushUp)

myEventQueueSystem.dispatch("Study") --> You will study math today
myEventQueueSystem.dispatch("Study") --> You will study music today
myEventQueueSystem.dispatch("Study") --> Event is none!
myEventQueueSystem.dispatch("WorkOut") --> You will work out squat 6 times today.
myEventQueueSystem.dispatch("Something") --> Event is none!
"""


from collections import deque
from typing import Callable, Dict

class Item:
    def __init__(self, data: Callable[[], str]):
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

    def enqueue(self, func: Callable[[], str]):
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

class EventQueue:
    def __init__(self):
        self.queue: Dict[str, Queue] = {}

    def push(self, event: str, func: Callable[[], str]):
        if self.event_exists(event):
            self.queue[event].enqueue(func)
        else:
            temp = Queue()
            temp.enqueue(func)
            self.queue[event] = temp

    def event_exists(self, event: str):
        return event in self.queue and self.queue[event].peek_front() is not None

    def run(self, event: str):
        if self.event_exists(event):
            print(self.queue[event].peek_front()())

    def dispatch(self, event: str):
        if self.event_exists(event):
            print(self.queue[event].dequeue()())
        else:
            print("Event is none!")

if __name__ == "__main__":
    math = lambda: "You will study math today"
    music = lambda: "You will study music today"
    squat = lambda: "You will work out squat 6 times today"
    push_up = lambda: "You will work out squat 20 Push-up today"

    my_event_queue_system = EventQueue()
    my_event_queue_system.push("Study", math)
    my_event_queue_system.push("Study", music)
    my_event_queue_system.push("WorkOut", squat)
    my_event_queue_system.push("WorkOut", push_up)

    my_event_queue_system.dispatch("Study")
    my_event_queue_system.dispatch("Study")
    my_event_queue_system.dispatch("Study")
    my_event_queue_system.dispatch("WorkOut")
    my_event_queue_system.dispatch("WorkOut")
    my_event_queue_system.dispatch("Something")
