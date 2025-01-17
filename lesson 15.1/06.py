harytlar = []
while True:
    print("\Dukan dolandyrmak ucin menu:")
    print("1.Harytlar gorkezmek")
    print("2.Harytar satyn almak")
    print("3.Taze haryt gosmak")
    print("4.Harydyn bahasyny uytgetmek")
    print("5.Harydy artdyrmak")
    print("6.Mukdary artdyrmak")
    print("7.Kassany gorkezmek")
    print("8.Cykmak")

    saylaw = input("Saylawynyzy girizin: ")
    if saylaw == "1":
      if not harytlar:
          print("Dukan bos!")
      else:
          print("Dukandaky ahli harytlar:")
          for haryt in harytlar:
              print(f"Ady:{haryt['ady']},Bahasy:{haryt['bahasy']} manat, Mukdary:{haryt['mukdary']} kg")
    elif saylaw == "2":
        ady = input("Satyn almak isleyan harydyn adyny girizin:")
        mukdary = float(input("Satyn almak isleyan mukdarynyzy (kg) girizin: "))

        tapyldy = False
        for haryt in harytlar:
            if haryt ['ady'] == ady:
                tapyldy = True
                if haryt['mukdary'] >= mukdar:
                    haryt['mukdary'] -= mukdary
                    jemi = mukdar * haryt ['bahasy']
                    print(f"Satyn alys gutardy! Jemi toleg: {jemi} manat")
                else:
                    print("Dukanda yeterlik haryt yok!")
                break
        if not tapyldy:
            print("Haryt tapylmady!")
    elif saylaw == "3":
        ady = input("Taze harydyn adyny girizin: ")
        bahasy = float(input("Harydyn bahasyny giizin (manat): "))
        mukdary = float(input("Harydyn mkdaryny girizin (kg): "))
        harytlar.append({"ady": ady, "bahasy": bahasy, "mukdary": mukdary})
        print("Taze haryt dukana gosuldy!")
    elif saylaw == "4":
        ady = input("Bahasyny uytgetmek isleyan harydyn adyny girizin: ")
        taze_baha = float(input("Taze bahany giizin (manat): "))
        tapyldy = False
        for haryt in harytlar:
            if haryt['ady'] == ady:
                tapyldy = True
                haryt['bahasy'] = taze_baha
                print("Harydyn bahasy tazelendi!")
                break
        if not tapyldy:
            print("Haryt tapylmady!")
    elif saylaw == "5":
        ady = input("Ayyrmak isleyan harydyn adyny girizin: ")
        tapyldy = False
        for haryt in harytlar:
            if haryt['ady'] == ady:
                tapyldy = True
                harytlar.remove(haryt)
                print("Haryt dukandan ayryldy!")
                break
        if not tapyldy:
            print("Harydyn tapylmady!")
    elif saylaw == "6":
        ady = input("Mukdary artdyrmak isleyan harydyn adyny girizin: ")
        gosmaca_mukdar = float(inpu("Nace kilogram gosmak isleyarsiniz? "))
        tapyldy = False
        for haryt in harytlar:
             if haryt['ady'] == ady:
                tapyldy = True
                haryt['mukdary'] += gosmaca_mukdar
                print("Harydyn mukdary tazelendi!")
                break
        if not tapyldy:
            print("Haryt tapylmady! ")
    elif saylaw == "7":
        jemi = 0
        for haryt in harytlar:
            jemi += haryt ['bahasy'] * haryt ['mukdary']
        print(f"Dukan kassasynyn jemi: {jemi} manat")
    elif saylaw == "8":
        print("Programmadan cykylyar... ")
        break
    else:
        print("Nadogryy saylaw! Tazeden synanysyn. ")