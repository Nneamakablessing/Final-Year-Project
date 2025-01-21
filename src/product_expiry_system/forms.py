from django import forms


class ProductRegistrationForm(forms.Form):
    product_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
        label="Product Name",
        required=True
    )
    product_code = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
        label="Product Code",
        required=True
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter product price'}),
        label="Price",
        required=True
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
        label="Quantity",
        required=True
    )
    expiry_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}),
        label="Expiry Date",
        required=True
    )
    barcode_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label="Product Barcode",
        required= False
    )
