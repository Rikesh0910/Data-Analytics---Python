""" list functions
lis1 = [2,4,6,8,3,7]

def list_sum(lis):
    total = 0
    for i in range(len(lis)):
        total += lis[i]
    return total;

print(list_sum(lis1))



lis1 = [2,4,6,8,3,7]

def find_largest(lis):
    largest = lis[0]
    for i in range(len(lis)):
        if lis[i] > largest:
            largest = lis[i]
    return largest

print(find_largest(lis1))



lis1 = [2,4,6,8,3,7]

def rev_list(lis):
    new_list = []
    lis_len = len(lis)
    for i in range(lis_len - 1, -1, -1):
        new_list.append(lis[i])
    return new_list

print(rev_list(lis1))



def prime_checker(n):
    if n < 2:
        return "the value is low to check for prime!"
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
print(prime_checker(9))



lis1 = [2,4,6,8]
lis2 = [3,5,8,4]

def find_common_el(li1, li2):
    common_el = []
    for i in range(len(li1)):
        if li1[i] in li2:
            common_el.append(li1[i])
    return common_el

print(find_common_el(lis1, lis2))



text = "apple orange apple banana orange apple"

words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


years_exp = {
    "rick" : 6,
    "sid" : 4,
    "john" : 7,
    "vicky" : 3,
    "mark" : 5
}

count = 0
index = 0

years_list = list(years_exp.items())
while count < 5 and index < len(years_list):
    key, value = years_list[index]
    if value > 5:
        print(key, value)
    index += 1
    count += 1


nums = [x for x in range(10)]

even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
print(even)


job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]
# My skills
my_skills = ['Python', 'SQL', 'Excel']
qualified_roles = []
for job in job_roles:
    qualified = True

    for skill in my_skills:
        if skill not in job["skills"]:
            qualified = False
            break

    if qualified:
        qualified_roles.append(job['role'])

print(qualified_roles)


even_chk = lambda x: "even" if x % 2 == 0 else "odd"
print(even_chk(6))


lis1 = [4,8,2,9,1,17,3]
lis1.sort()
def binary_search(lis, tar):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == tar:
            return mid
        elif lis[mid] < tar:
            left = mid + 1
        elif lis[mid] > tar:
            right = mid - 1
    return -1

print(binary_search(lis1, 2))

"""

from datasets import load_dataset
