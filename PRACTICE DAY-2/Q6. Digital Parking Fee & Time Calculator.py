entry = input("Enter Entry Time (HH:MM): ")
exit = input("Enter Exit Time (HH:MM): ")
entry_hour = int(entry[0:2])
entry_minute = int(entry[3:5])
exit_hour = int(exit[0:2])
exit_minute = int(exit[3:5])
entry_total = entry_hour * 60 + entry_minute
exit_total = exit_hour * 60 + exit_minute
if exit_total < entry_total:
    exit_total = exit_total + 24 * 60
duration = exit_total - entry_total
hours = duration // 60
minutes = duration % 60
billable_hours = (duration + 59) // 60
if billable_hours <= 1:
    fee = 30
else:
    fee = 30 + (billable_hours - 1) * 20
print("\nParking Duration :", hours, "hours", minutes, "minutes")
print("Billable Hours   :", billable_hours)
print("Parking Fee      : ₹", fee)