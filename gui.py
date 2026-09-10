import streamlit as st


from blood_donor_view import BloodDonorManagement

donor_instance=BloodDonorManagement()

tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Blood Donor")
    name=st.text_input("Blood Donor Name=")
    # blood_group=st.text_input("Blood Group=")
    #blood group using option
    blood_group=st.selectbox("Please select your blood group",["A+","B+","O-","AB+","A-","B-","AB-","O+"])
    phone=st.text_input("Phone Number=")
    city=st.text_input("City Name=")
    # last_donation=st.text_input("Last donation date=(yyyy/mm/dd)")
    #date using selection
    last_donation = st.date_input("Last donation date=(yyyy/mm/dd)")
    if st.button("Add New Blood Donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor Added Successfully")

with tab2:
    st.title("View Blood Donor Details")
    records=donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("Record not found")