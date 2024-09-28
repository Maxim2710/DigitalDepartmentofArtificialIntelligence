n = int(input().strip())

registered_users = set(input().strip().split())

k = int(input().strip())

registration_requests = input().strip().split()

unique_requests = set()

for request in registration_requests:
    if request not in registered_users:
        unique_requests.add(request)

sorted_requests = sorted(unique_requests)

print(' '.join(sorted_requests))
