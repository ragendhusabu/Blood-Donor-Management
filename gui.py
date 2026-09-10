import streamlit as st
from blood_donor_views import BloodDonorManager

donor_instance =BloodDonorManager()

tab1,tab2 = st.tabs(["ADD  ","VIEW  "])

with tab1:
    st.title("Add Blood New Donor")
    name = st.text_input("Blood Donor Name ")
    blood_group = st.text_input("Blood Group ")
    phone = st.text_input("Primary Contact Number ")
    city = st.text_input("Place ")
    last_donation = st.text_input("Last Donation Date ")
    if st.button("Add"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor Added Successfully")
with tab2:
    st.title("View Blood Donor Details")