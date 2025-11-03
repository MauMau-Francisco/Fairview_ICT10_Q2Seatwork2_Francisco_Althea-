from pyscript import document, display
def general_average(e):
    # identify values
    math = float(document.getElementById('math').value)
    science = float(document.getElementById('science').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

#input fields
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
   

    #calculation
    weighted_sum = (math * 5 + science * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = 21
    gwa = weighted_sum / total_units

# List of subjects
    subjects = ['math', 'science', 'english', 'filipino', 'ict', 'pe']

    # results 
    summary = f"""
    {subjects[0]}: {science:.0f} 
    {subjects[1]}: {math:.0f} 
    {subjects[2]}: {science:.0f}
    {subjects[3]}: {english:.0f} 
    {subjects[4]}: {filipino:.0f} 
    {subjects[5]}: {ict:.0f} 
    """

    display(f'Name: {first_name} {last_name}', target='student_info_text')
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')