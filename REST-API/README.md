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
            "user" : "Josh",
            "temperature" : 72,
            "LED": "red"
        },
        {
            "user" : "Gon",
            "temperature" : 69,
            "LED": "oyster"
        }
    ]
```

### Registering a new user

**Definition**

`POST /users`

**Arguments**

- `"user":string` the username chosen for the user
- `"temperature":integer` the temperature set for the hot beverage
- `"LED":string` the desired colour for the LED

**Response**

- `201 Created` on success

```json
{
    "user" : "Gon",
    "temperature" : 68,
    "LED": null,
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
    "temperature" : 69,
    "LED": "oyster"
}
```

## Delete a user

**Definition**

`DELETE /users/<user_name>`

**Response**

- `404 Not Found` if the user does not exist
- `204 No Content` on success

