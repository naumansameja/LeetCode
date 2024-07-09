class Solution:
    def averageWaitingTime(self, customers) -> float:
        customers_count = 0
        current_time = customers[0][0]
        total_waiting_time = 0
        for customer in customers:
            customers_count += 1
            if customer[0] > current_time:
                current_time = customer[0]
            
            current_time += customer[1]
            total_waiting_time += (current_time-customer[0])
        return total_waiting_time / customers_count