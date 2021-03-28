# User Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List of all users

**Definition**

`GET /users`

**Response**
- `200 OK` on success

```json
    [
        {
            "user": "Yuji",
            "des_temp": "62",
            "range": "5",
            "C_RGB": "(0, 0, 255)",
            "P_RGB": "(0, 255, 0)",
            "H_RGB": "(255, 0, 0)"
        },
        {
            "user": "Todo",
            "des_temp": "59",
            "range": "3",
            "C_RGB": "(255, 69, 0)",
            "P_RGB": "(152, 251, 152)",
            "H_RGB": "(255, 0, 255)"
        }
    ]
```

### Registering a new user

**Definition**

`POST /users`

**Arguments**

- `"user":string` the username chosen for the user
- `"des_temp":integer` the desired temperature set for the hot beverage
- `"range":integer` the range for the desired temperature
- `"C_RGB":string` the LED colour that indicates the beverage is below the desired temperature
- `"P_RGB":string` the LED colour that indicates the beverage is at the desired temperature
- `"H_RGB":string` the LED colour that indicates the beverage is above the desired temperature

**Response**

- `201 Created` on success

```json
{
    "user": "Todo",
    "des_temp": "59",
    "range": "3",
    "C_RGB": "(255, 69, 0)",
    "P_RGB": "(152, 251, 152)",
    "H_RGB": "(255, 0, 255)"
}
```

## Lookup user's details

`GET /users/<user_name>`

**Response**

- `404 Not Found` if the user does not exist
- `200 OK` on success

```json
{
    "user" : "Gon",
    "des_temp": "63",
    "range": "5",
    "C_RGB": "(255, 69, 0)",
    "P_RGB": "(152, 251, 152)",
    "H_RGB": "(255, 0, 255)",
    "temperature": "19.37 C",
    "volume": "23 ml"
}
```

## Delete a user

**Definition**

`DELETE /users/<user_name>`

**Response**

- `404 Not Found` if the user does not exist
- `204 No Content` on success

