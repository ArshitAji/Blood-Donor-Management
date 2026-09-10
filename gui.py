import streamlit as st


from blood_donor_view import BloodDonorManagement

donor_instance=BloodDonorManagement()

tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Blood Donor")
    name=st.text_input("Blood Donor Name=")
    blood_group=st.text_input("Blood Group=")
    phone=st.text_input("Phone Number=")
    city=st.text_input("City Name=")
    last_donation=st.text_input("Last donation date=")
    if st.button("Add New Blood Donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor Added Successfully")

with tab2:
    st.title("View Blood Donor Details")