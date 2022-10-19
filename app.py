import streamlit as st
from PIL import Image


def header(url):
     st.markdown(f'<p style="background-color:#FFFFFF;color:#006400;font-size:40px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)



col1, col2, col3 = st.columns([2,20,1])

with col1:
    st.write("")

with col2:
    st.title('New York Taxi Price Prediction')

with col3:
    st.write("")


col1, col2, col3 = st.columns([1.5,1,1])

with col1:
    st.write("")

with col2:
    img = Image.open('nyc_taxi.jpg')
    st.image(img,width=150)
with col3:
    st.write("")




a = st.number_input('No. of passengers: ',min_value=1,max_value=7)
b = st.number_input('Trip distance(in Km): ',key="b",min_value=1.0,max_value=1000.0)


x = st.radio("Final rate code ID: ",('Standard rate','JFK','Newark','Nassau or Westchester','Negotiated fare','Group ride'))

if(x=='Standard rate'):
    c=1
elif(x=='JFK'):
    c=2
elif(x=='Newark'):
    c=3
elif(x=='Nassau or Westchester'):
    c=4
elif(x=='Negotiated fare'):
    c=5
elif(x=='Group ride'):
    c=6



# This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, 
# aka “store and forward,” because the vehicle did not have a connection to the server.
new_user = st.radio("New user: ",('Yes','No'))

if(new_user=='Yes'):
    d=1
else:
    d=0





list_a = [142, 236, 166, 114,  68, 138, 233, 238, 141, 234, 246,  43, 239,
       148, 237,   7, 107, 263, 161,  79, 170, 162,   4, 262, 249, 132,
       137,  90,  45,  70,  48, 211, 113, 164,  50, 265,  88, 186, 144,
       224,  95,  24, 158,  74, 163,  75, 229, 209, 264, 140, 219, 232,
       151, 256, 231,  87, 116,  65, 188,  42,  13,  33,  41, 220, 146,
       100, 261, 125, 152, 127, 143, 243,  66, 260, 181, 195, 112, 129,
        10, 226,  25, 255, 244,  12, 168, 230, 189,  97,  82, 190,  52,
        49,  61, 145, 223, 202, 228, 179,  36,  40, 159,  80,  17, 167,
       208,  69, 254, 213, 193,  77,  37, 225, 171, 106,  93, 247, 165,
       117, 212, 250,  14, 157, 198,  83, 169, 136, 217, 173, 123, 160,
         3,  1,  76,  89,  22,  39,  86,  18,  28, 252, 227, 135,  91,
       124,  38, 216, 119, 205,  81, 122, 194,  92, 133,  35, 134, 177,
       215, 147, 248,  63,  47, 210, 197, 201, 131, 200,  56,   5, 130,
       191,  85, 218,  51,  46, 149, 241, 139, 235,  71, 102,  62, 174,
        72, 182,  11,  29, 183,  67, 155,  54, 196,   8,  55,  53,  64,
       180,  34,  60, 120,  44, 257,  78, 207, 242, 184, 153, 175, 185,
        15,  19,  26, 258, 121,  57, 203, 101, 128, 154, 206,  23, 192,
        21, 126, 108,  96,  94, 259,  16,   9, 178,   6, 222,  98, 221,
       150,  73,  20,  32,  31,  58,  27, 245, 214,  30,   2, 156, 172,
       253, 240,  59, 118, 105, 111, 109, 176, 115]
list_a.sort()
pickup_location_ID = st.selectbox("Pick up location ID :",list_a)
e = pickup_location_ID






list_b = [236,  42, 166,  68, 163, 161,  87, 152, 141, 229,  90, 113,  79,
       140, 151, 107,   7, 263,  43,  24, 233, 238,  48, 237, 249, 186,
        92, 262, 170,  74,  10, 112,   4,  45, 148,  47, 142, 137, 261,
       246,  41,  36, 239, 168, 243,  61, 153, 231, 139, 265, 114,  97,
       255, 211, 164, 180, 144, 256,  13, 134, 143, 196, 125,  50, 162,
       234,  65, 181,  83,  40, 193, 130, 226, 202,  56,  70,  80,  17,
        85, 223, 241, 224, 179,  18, 244, 157, 189, 129,  33, 106, 158,
       232, 220, 116,  82,  25, 197, 169,  72,  88,  35,  49,  75, 177,
       160, 225, 213, 127, 264, 146,  89,  51, 257, 147, 100, 228,  39,
       145, 198,  37,  66,  63, 102, 173, 209, 260, 218, 132,   8, 188,
        86,  15,  69,  73, 219, 252,  71,  95,  26, 185, 119, 248, 217,
        28,  52, 120, 138, 212, 216,  91, 133, 192, 117,  14,  67,  76,
       123,  32,  54, 136, 175, 159, 215, 222,  23, 178, 230, 121,  64,
        60,  78,  16,  62, 200, 194,   9, 247, 210, 174, 165, 254,  21,
       208,  12, 258, 171, 259, 155,  11,  22, 167, 195,  20,  34, 149,
       240,  19, 205, 227, 191, 182,   1,  77,  57,  81, 126, 115, 190,
       108, 235, 250,  38,  31,  94, 150, 183,  55,  53, 131, 203, 128,
       135,   3, 124, 187, 206, 201, 242,  93,  98,   5,  30, 214,  29,
       101,   2, 122,  44,   6,  58,  27, 154, 111, 109,  96, 251, 207,
       184, 118, 172, 156, 204, 221,  46, 253,  59,  99, 176, 245,  84,
       105]
list_b.sort()
DropOff_location_ID = st.selectbox("Drop off location ID :",list_b)
f = DropOff_location_ID




payment_type = st.radio("Mode of payment: ",('Credit card','Cash','No charge','Dispute','Unknown','Voided Trip'))
if(payment_type == 'Credit card'):
    g=1
elif(payment_type == 'Cash'):
    g=2
elif(payment_type == 'No charge'):
    g=3
elif(payment_type == 'Dispute'):
    g=4
elif(payment_type == 'Unknown'):
    g=5
elif(payment_type == 'Voided Trip'):
    g=6




# Improvement surcharge
h = 0.3




# Congestion Surcharge
congestion_surcharge = st.radio("Congestion surcharge: ",('0.75$','2.5$','Not applicable'))
if congestion_surcharge == '0.75$':
    i=0.75
elif congestion_surcharge == '2.5$':
    i=2.5
else:
    i=0



# Airport fee
airport_fee = st.radio("Airport Fee ($1.25 fixed): ",('Yes','No'))
if airport_fee == 'Yes':
    j=1.25
else:
    j=0



# Week day
week_day = st.selectbox("Day of week : ",('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'))
if week_day == 'Monday':
    k=0
elif week_day == 'Tuesday':
    k=1
elif week_day == 'Wednesday':
    k=2
elif week_day == 'Thursday':
    k=3
elif week_day == 'Friday':
    k=4
elif week_day == 'Saturday':
    k=5
elif week_day == 'Sunday':
    k=6





time = st.selectbox("Time of the day : ",('00:00','01:00','02:00','03:00','04:00','05:00','06:00',
'07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00',
'20:00','21:00','22:00','23:00'))

if time == '00:00':
    l = 0
elif time == '01:00':
    l = 1
elif time == '02:00':
    l = 2
elif time == '03:00':
    l = 3
elif time == '04:00':
    l = 4
elif time == '05:00':
    l = 5
elif time == '06:00':
    l = 6
elif time == '07:00':
    l = 7
elif time == '08:00':
    l = 8
elif time == '09:00':
    l = 9
elif time == '10:00':
    l = 10
elif time == '11:00':
    l = 11
elif time == '12:00':
    l = 12
elif time == '13:00':
    l = 13
elif time == '14:00':
    l = 14
elif time == '15:00':
    l = 15
elif time == '16:00':
    l = 16
elif time == '17:00':
    l = 17
elif time == '18:00':
    l = 18
elif time == '19:00':
    l = 19
elif time == '20:00':
    l = 20
elif time == '21:00':
    l = 21
elif time == '22:00':
    l = 22
elif time == '23:00':
    l = 23



if(st.button('Calculate Fare')):
       Price = (7.82247612e-02*a) + (2.17325361e+00*b) + (1.41813923e-01*c) + (1.85990839e-02*d) + (1.76894534e-04*e) - (1.85810665e-04*f) - (3.13545726e-01*g) - (1.18537646e+02*h) - (1.59796702e+00*i) + (2.13953431e+00*j) - (1.33644855e-02*k) - (1.67614529e-02*l) + 45.420248128847675
       st.snow()
       st.text('The predicted taxi fare is')
       header('{}$'.format(round(Price,2)))