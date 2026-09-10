import streamlit as st
from numpy.core import records

from blood_donor_views import BloodDonorManager

donor_instance =BloodDonorManager()

tab1,tab2 = st.tabs(["ADD  ","VIEW  "])

with tab1:
    st.subheader("Add Blood New Donor")
    name = st.text_input("Blood Donor Name ")
    blood_group = st.selectbox("Select your Blood Group ",["--","A+","B+","O+","AB+","A-","B-","O-","AB-"])
    phone = st.text_input("Primary Contact Number ")
    city = st.text_input("Place ")
    last_donation = st.date_input("Last Donation Date")
    if st.button("Add"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor Added Successfully")
with tab2:
    st.subheader("View Blood Donor Details")
    records =donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Records Found..!")