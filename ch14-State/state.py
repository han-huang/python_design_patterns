from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition

# http://pythonhosted.org/state_machine/

@acts_as_state_machine # 裝飾器指定一個狀態機類
class Process: # 進程模型
    # 指定狀態，一個狀態就是一個 State，可用帶時態的單詞命名
    created = State(initial=True) # 創建狀態, initial=True 指定為初始狀態
    waiting = State() # 等候狀態
    running = State() # 運行狀態
    terminated = State() # 停止狀態
    blocked = State() # 阻塞狀態
    swapped_out_waiting = State() # 換出並等候狀態
    swapped_out_blocked = State() # 換出並阻塞狀態

    # 指定狀態轉換，一個狀態轉換就是一個 Event，
    # 裝換也是一個動作，可用作為動詞的單詞命名
    # 等待事件，從創建狀態，運行狀態，阻塞狀態和喚醒並等候狀態變為等候狀態
    wait = Event(from_states=(created, running, blocked,
                              swapped_out_waiting), to_state=waiting)
    # 運行事件，從等候狀態變為運行狀態
    run = Event(from_states=waiting, to_state=running)
    # 停止事件，從運行狀態變為終止狀態
    terminate = Event(from_states=running, to_state=terminated)
    # 阻塞事件，從運行狀態，喚醒並阻塞狀態變為阻塞狀態
    block = Event(from_states=(running, swapped_out_blocked),
                  to_state=blocked)
    # 換出並等待事件，從等候狀態變為換出並等候狀態
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    # 換出並阻塞事件，從阻塞狀態變為換出並等候狀態
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after('wait') # 在 wait 轉換之後運行
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run') # 在 run 轉換之後運行
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate') # 在 terminate 轉換之前運行
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block') # 在 block 轉換之後運行
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait') # 在 swap_wait 轉換之後運行
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block') # 在 swap_block 轉換之後運行
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err: # 狀態轉換失敗
        print('Error: transition of {} from {} to {} failed'.format(process.name,
                                                                    process.current_state, event_name))


def state_info(process):
    print('state of {}: {}'.format(process.name, process.current_state)) # current_state 當前的狀態


def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

if __name__ == '__main__':
    main()
