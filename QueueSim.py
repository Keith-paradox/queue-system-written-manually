import random  # importing random to use the random number generator

while True:
    minute = input("Please enter the total minutes to run: ")  # asking for how many minutes/loops the program will run
    try:
        minute = int(minute)  # using try/except function to change the minute to integer without any errors
        break
    except ValueError:  # for catching the error when the user typed in other things other than integer
        print("Invalid input. Try again.")

i = 1  # variable for the loop to run the chosen amount of time
queue_array = []  # array for the queue
cannot_sent = []  # array of 25% of the messages that cannot be sent
messages_sent = 0  # total number of messages sent successfully
msg = 1  # variable used to add each messages to the queue
attempts = {}  # the dictionary containing messages and the attempt they are sent successfully on
msg_processed = 0  # total number of messages arrived
msg_in_queue = 0  # the amount of messages in the queue for each minute
requeue_amt = 0  # total number of messages that have to be requeue

while i <= minute:  # looping the amount of times user typed in
    messages_per_min = random.randint(0, 60)  # random generating amount of messages arrived in each minute with the
    # average of 30
    msg_processed += messages_per_min  # adding total number of messages processed each minute

    i += 1
    m = 1
    while m <= messages_per_min:  # a loop to add each messages into the queue
        queue_array.append(msg)  # adding a message to queue
        m += 1
        msg += 1

    msg_in_queue += len(queue_array)  # adding the length of queue to see amount of message in a queue each minute
    for x in queue_array:  # a loop to create a dictionary with each message and attempts they are sent on
        if x not in attempts:  # checking if the message is in the dictionary
            attempts[x] = 0  # if not add the message in the dictionary with the attempt being one

    deduct = round((25*messages_per_min)/100, 0)  # calculate the 25% from all the messages sent in a minute

    d = 1
    while d <= deduct:  # loop to choose 25% of random messages from queue to deduct later on
        random_num = random.choice(queue_array)  # choosing random message from the queue
        if random_num in cannot_sent:  # making sure there's no duplicates chosen randomly
            continue
        else:
            pass
        d += 1

        cannot_sent.append(random_num)  # adding that random number into an array

    dequeue = 1
    dequeue_random = random.randint(0, 30)  # random generating the number of messages to dequeue
    if len(queue_array) > dequeue_random:  # checking if the amount of messages to be dequeue is greater than the
        # messages in the queue to avoid error
        while dequeue <= dequeue_random:  # loop to dequeue messages based on the dequeue amount
            dequeue += 1
            attempts[queue_array[0]] += 1  # marking the message is sent once using dictionary
            queue_array.pop(0)  # removing the message from the queue
            messages_sent += 1  # to check how many messages have been sent
        cannot_sent.sort()  # sorting out the array of randomly chosen 25% messages that cant be sent
        for x in cannot_sent:  # loop to requeue the messages that cant be sent
            if x not in queue_array:  # if the message that cant be sent is sent it's going to requeue
                queue_array.append(x)  # requeue-ing that message
                messages_sent -= 1  # a message got requeue so reducing the amount of messages sent
                requeue_amt += 1  # checking how many messages got to requeue
    else:
        messages_sent = messages_sent + len(queue_array) - deduct
        # all the message in the queue got sent except the 25%
        queue_array.clear()  # clearing cause all of it got sent
        cannot_sent.sort()  # sorting out the 25% of the messages that cant be sent
        for x in cannot_sent:  # a loop to requeue the message that cant be sent
            queue_array.append(x)  # requeue-ing the messages
            requeue_amt += 1  # checking how many messages got to requeue

    cannot_sent.clear()  # clearing the array so there wont be any duplicates when it got added in the next loop

first = 0  # variable to check how many messages got sent in first attempt
second = 0  # variable to check how many messages got sent in second attempt
third = 0  # variable to check how many messages got sent in third attempt
fourth = 0  # variable to check how many messages got sent in fourth attempt
fifth = 0  # variable to check how many messages got sent in fifth attempt

for key, value in attempts.items():  # a loop to check inside the dictionary for first, second, thrid, fourth,
    # fifth attempts
    if value == 1:
        first += 1
    elif value == 2:
        second += 1
    elif value == 3:
        third += 1
    elif value == 4:
        fourth += 1
    elif value == 5:
        fifth += 1

# printing outputs
print()
print("Total number of messages processed\t\t\t\t\t: ", msg_processed)
print("Average arrival rate\t\t\t\t\t\t\t\t: ", round(msg_processed/minute, 2))
print("Average number of messages sent per minute\t\t\t: ", round(messages_sent/minute, 2))
print("Average number of messages in the queue per minute\t: ", round(msg_in_queue/minute, 2))
print("Number of messages sent on 1st attempt\t\t\t\t: ", first)
print("Number of messages sent on 2nd attempt\t\t\t\t: ", second)
print("Number of messages sent on 3rd attempt\t\t\t\t: ", third)
print("Number of messages sent on 4th attempt\t\t\t\t: ", fourth)
print("Number of messages sent on 5th attempt\t\t\t\t: ", fifth)
print("Average number of times messages had to be requeued: ", round(requeue_amt/minute, 2))
