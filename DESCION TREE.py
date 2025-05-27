# Play Golf dataset simplified (only Outlook feature)
# Outlook -> Play
# Sunny -> No if Humidity high else Yes (simplified)
# Overcast -> Yes always
# Rain -> Yes if Wind weak else No (simplified)

def play_golf():
    print("Enter today's weather details:")
    outlook = input("Outlook (Sunny/Overcast/Rain): ").strip().capitalize()
    
    # If outlook is Overcast, always Play = Yes
    if outlook == "Overcast":
        print("\n🎯 Decision: Play Golf = Yes (Overcast day always good)")
        return
    
    humidity = None
    wind = None
    
    if outlook == "Sunny":
        humidity = input("Humidity (High/Normal): ").strip().capitalize()
        if humidity == "High":
            print("\n🎯 Decision: Play Golf = No (Sunny + High Humidity)")
        else:
            print("\n🎯 Decision: Play Golf = Yes (Sunny + Normal Humidity)")
        return
    
    if outlook == "Rain":
        wind = input("Wind (Weak/Strong): ").strip().capitalize()
        if wind == "Weak":
            print("\n🎯 Decision: Play Golf = Yes (Rain + Weak Wind)")
        else:
            print("\n🎯 Decision: Play Golf = No (Rain + Strong Wind)")
        return

    print("\n⚠️ Invalid input or case not covered.")

play_golf()
