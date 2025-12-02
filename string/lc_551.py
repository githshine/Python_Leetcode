# 551. Student Attendance Record I
# The student is eligible for { an attendance award } if they meet both of the following criteria:
# 1) The student was absent ('A') for strictly fewer than 2 days total.
# 2) The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

class Solution:
    def checkRecord(self, s: str) -> bool:
        totalAbsent = 0
        previousDayLate = False
        conLateDays = 0
        for att in s:
            if att == 'A':
                totalAbsent += 1
                previousDayLate = False
                if totalAbsent >= 2:
                    return False
            elif att == 'L':
                conLateDays = conLateDays + 1 if conLateDays == 0 or previousDayLate == True else 1
                previousDayLate = True 
                if conLateDays >= 3:
                    return False
            else:
                previousDayLate = False
        return True
            
        

if __name__ == "__main__":
    obj = Solution()
    print(obj.checkRecord('PPALLP')) # true
    print(obj.checkRecord('PPALLPL')) # true
    print(obj.checkRecord('PPALLL')) # false