text = """
             &kp GRAVE    &kp N1       &kp N2       &kp N3       &kp N4       &kp N5                                              &kp N6       &kp N7       &kp N8       &kp N9       &kp N0       &kp AMPERSAND
             &kp ESC      &kp Q        &kp W        &kp F        &kp P        &kp B                &kp N1            &kp N2       &kp J        &kp L        &kp U        &kp Y        &kp COLON    &kp BSPC
             &kp TAB      &kp A        &kp R        &kp S        &kp T        &kp G                &kp N4            &kp N3       &kp M        &kp N        &kp E        &kp I        &kp O        &kp SQT
             &kp LSHFT    &kp Z        &kp X        &kp C        &kp D        &kp V                &kp C_MUTE        &kp N5       &kp K        &kp H        &kp COMMA    &kp DOT      &kp FSLH     &kp RSHFT
                                       &kp LGUI     &kp ESC      &kp SPACE    &mo TAB              &kp RET           &kp ENTER    &kp ENTER    &kp BSPC     &kp DEL      &kp RGUI
"""


template = """
             {:12}       {:12}       {:12}       {:12}       {:12}       {:12}               {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}
             {:12}       {:12}       {:12}       {:12}       {:12}       {:12}               {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}
             {:12}       {:12}       {:12}       {:12}       {:12}       {:12}               {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}
             {:12}       {:12}       {:12}       {:12}       {:12}       {:12}               {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}       {:12}
                                     {:12}       {:12}       {:12}       {:12}               {:12}       {:12}       {:12}       {:12}       {:12}       {:12}
"""

out = []
for line in text.split("\n"):
    if line.strip():
        keys = line.strip().split("&")
        if len(keys) < 12:
            keys = ["",""] + keys
        for idx, key in enumerate(keys[:]):
            if idx == 7:
                print(f"{'':<8}", end="")
            if key.strip():
                print(f"&{key.strip():<12}", end="")
                out.append(key.strip())
            else:
                print(f"{'':<13}", end="")
        print()

print(out)
print(len(out))
print(template.format(*out))
