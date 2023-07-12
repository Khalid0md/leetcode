from collections import deque
class Sol:
    def solution(S, K):
        array = S.split(" ")
        messages = [""]
        for word in array:
            if len(messages[-1]) + len(word) < K:
                if len(messages[-1]) == 0:
                    messages[-1] = word
                    continue
                messages[-1] = messages[-1] + " " + word
            elif len(word) <= K:
                messages.append(word)
            else:
                return -1
        return len(messages)
    
        

        

        

    
    print(solution("SMS messages are terribly short", 12))