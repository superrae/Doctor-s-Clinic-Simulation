import random
from Queue import *


class Clinic:
    def __init__(self, patients):
        self.patient_rate = patients
        self.current_patient = None
        self.remaining_time = 0

    def busy(self):
        if self.current_patient != None:
            return True
        else:
            return False

    def start_next(self, new_patient):
        self.current_patient = new_patient
        self.remaining_time = round(((new_patient.get_age() / self.patient_rate) * 60), 2)


    def tick(self):
        if self.current_patient != None:
            self.remaining_time -= 1
            if self.remaining_time == 0:
                self.current_patient = None

class Patient:
    def __init__(self, time):
        self.time_stamp = time
        self.age = random.randrange(20, 61)

    def get_stamp(self):
        return self.time_stamp

    def get_age(self):
        return self.age

    def waiting_time(self, current_time):
        return current_time - self.time_stamp

def simulation(total_seconds, patient_rate_per_minute):
    clinic = Clinic(patient_rate_per_minute)
    queue_of_patients = Queue()
    waiting_seconds = []
    for current_second in range(total_seconds):
        if random.randrange(1, 361) == 360:
            p = Patient(current_second)
            queue_of_patients.enqueue(p)

        if (not clinic.busy()) and (not queue_of_patients.isEmpty()):
            next_p = queue_of_patients.dequeue()
            waiting_seconds.append(next_p.waiting_time(current_second))
            clinic.start_next(next_p)
        clinic.tick()
    print("average waiting time = ", round((sum(waiting_seconds) / len(waiting_seconds)), 2), " seconds, ", queue_of_patients.size(), "patients remaining.")

for i in range(10):
    simulation(14400, 5)



