import threading

class SumThread:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def calculate_sum(self):
        total = 0
        for i in range(self.start, self.end + 1):
            total += i
        print(f'{self.name}: {self.start}부터 {self.end}까지의 합 = {total}')

# 각 범위에 대해 스레드 생성
sum1 = SumThread(1, 1000, '[스레드1]')
sum2 = SumThread(1, 100000, '[스레드2]')
sum3 = SumThread(1, 10000000, '[스레드3]')

# 스레드 객체 생성
th1 = threading.Thread(target=sum1.calculate_sum)
th2 = threading.Thread(target=sum2.calculate_sum)
th3 = threading.Thread(target=sum3.calculate_sum)

# 스레드 시작
th1.start()
th2.start()
th3.start()

# 메인 스레드가 모든 스레드가 끝날 때까지 기다림
th1.join()
th2.join()
th3.join()

print("모든 합 계산이 완료되었습니다.")
