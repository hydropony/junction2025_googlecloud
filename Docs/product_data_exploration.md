# Product Data Exploration (Sample)

- File: `valio_aimo_product_data_junction_2025.json`
- Sample size: 5000 rows

## Columns and non-null ratios (top)

| column | non_null_ratio |
|---|---|
| salesUnit | 1.000 |
| baseUnit | 1.000 |
| category | 1.000 |
| allowedLotSize | 1.000 |
| deleted | 1.000 |
| vendorName | 1.000 |
| synkkaData | 1.000 |
| units | 1.000 |
| deposits | 1.000 |
| countryOfOrigin | 0.999 |
| temperatureCondition | 0.990 |
| salesUnitGtin | 0.988 |
| substitutions | 0.013 |

## Candidate feature fields (auto-detected)

- sku: salesUnitGtin
- name: vendorName
- category: category
- supplier: vendorName
- temperature: temperatureCondition
- pack: allowedLotSize
- unit: salesUnitGtin, salesUnit, baseUnit, units

## Sample rows

```json
[
  {
    "salesUnitGtin": "6409460002724",
    "salesUnit": "RAS",
    "baseUnit": "RAS",
    "category": "17301",
    "allowedLotSize": 0.01,
    "deleted": false,
    "temperatureCondition": 4.0,
    "vendorName": "ATRIA SUOMI OY TUORE",
    "countryOfOrigin": "fi",
    "synkkaData": {
      "gtin": "6409460002724",
      "lastUpdated": "2025-05-20T11:02:36+0300",
      "mediasLastUpdated": "2025-09-15T09:55:55+0300",
      "countriesOfOrigin": [
        "246"
      ],
      "names": [
        {
          "value": "Forssan Potato Salad 400g",
          "language": "en"
        },
        {
          "value": "Forssan Perunasalaatti 400g",
          "language": "fi"
        },
        {
          "value": "Forssan Potatissallad 400g",
          "language": "sv"
        }
      ],
      "materialAdditionalDescriptions": [],
      "marketingTexts": [
        {
          "value": "This rich potato salad is a hearty salad which is perfect for both weekday dinners and parties. Traditionally potato salad is a part of May Day festivities or New Years celebrations. It also makes for a great side for grilled foods. The Forssa-Style Potato Salad is made with fresh mayonnaise, potatoes, tasty pickles, cucumber, and onions. You could also use this Potato Salad as a rich sandwich filling or for a sandwich cake. The Potato Salad can be customized with fresh herbs or smoked fish, ham, or why not cheese cubes! The Forssa-Style Potato Salad can niftily be brought along for a picnic or an outing in its original packaging. You should note, however, that the Potato Salad does not keep for many hours in warm weather, as it should be kept in the refrigerator like other mayonnaise-based salads.",
          "language": "en"
        },
        {
          "value": "Täyteläinen perunasalaatti on ruokaisa salaatti, joka sopii niin arkeen kuin juhlaan. Perinteisesti perunasalaatti tarjoillaan juhlapöydässä vappuna ja uutena vuotena. Se on myös mainio lisuke grilliherkkujen kylkeen. Forssan Perunasalaatti on valmistettu tuoremajoneesista, perunoista, maukkaasta säilykekurkusta, tuorekurkusta ja sipulista. Perunasalaatti sopii myös ruokaisaksi leivän täytteeksi tai vaikkapa voileipäkakun väliin. Perunasalaattia voi tuunata tuoreilla yrteillä tai savukalalla, kinkulla tai vaikkapa juustokuutioilla. Forssan perunasalaatti kulkee mainiosti mukana piknikille tai eväsretkelle alkuperäispakkauksessaan. Kannattaa kuitenkin huomioida, että perunasalaatti ei säily lämpimässä useita tunteja, vaan se tulee säilyttää jääkaapissa kuten muutkin majoneesipohjaiset salaatit.",
          "language": "fi"
        },
        {
          "value": "Denna fylliga potatissallad är en matig sallad som passar i såväl vardagen som vid fester. Potatissallad serveras traditionellt på festbordet på valborg och nyår. Den är även ett utmärkt tillbehör intill grillmaten. Forssan Potatissallad är gjord på färskmajonnäs, potatis, smakrik inlagd gurka, färsk gurka och lök. Potatissallad passar också som matigt pålägg på bröd eller till exempel i en smörgåstårta. Du kan ändra potatissalladen efter egen smak med färska örter, rökt fisk, skinka eller till exempel med tärnad ost. Forssan potatissallad går utmärkt att ta med till picknicken i sin originalförpackning. Observera dock att potatissalladen inte håller i värme i flera timmar utan måste förvaras i kylskåp, liksom andra majonnäsbaserade sallader.",
          "language": "sv"
        }
      ],
      "keyIngredients": [
        {
          "value": "potato 56 % (Finland), mayonnaise (rapeseed oil, water, vinager, EGG YOLK, sugar, modified corn starch, iodised salt, preservative (potassium sorbate, sodium benzoate), maltodextrin, spices (MUSTARD SEED, white pepper)), cucumber, pickled cucumber (cucumber, flavors (incl. MUSTARD SEED), sweetener saccharin), onion",
          "language": "en"
        },
        {
          "value": "peruna 56 % (Suomi), majoneesi (rypsiöljy, vesi, etikka, KANANMUNANKELTUAINEN, sokeri, muunnettu maissitärkkelys, jodioitu suola, säilöntäaineet (kaliumsorbaatti, natriumbentsoaatti), maltodekstriini, mausteet (SINAPINSIEMEN, valkopippuri)), kurkku, säilykekurkku (kurkku, aromit (mm. SINAPINSIEMEN), makeutusaine sakariini), sipuli",
          "language": "fi"
        },
        {
          "value": "potatis 56 % (Finland), majonnäs (rypsolja, vatten, ättika, ÄGGULA, socker, modifierad majsstärkelse, joderat salt, konserveringsmedel (kaliumsorbat, natriumbensoat), maltodextrin, kryddor (SENAPSFRÖN, vitpeppar)), gurka, konserverad gurka (gurka, aromer (bl.a. SENAPSFRÖN), sötningsmedel sackarin), lök",
          "language": "sv"
        }
      ],
      "storageInstructions": [
        {
          "value": "Storage temperature under +6 °C",
          "language": "en"
        },
        {
          "value": "Säilytys alle +6 °C",
          "language": "fi"
        },
        {
          "value": "Förvaring under +6 °C",
          "language": "sv"
        }
      ],
      "preparationInstructions": [],
      "disposalInformations": [
        {
          "value": "Sorted as plastic.",
          "language": "en"
        },
        {
          "value": "Muovi ei kuulu luontoon. Laita pakkaus muovinkeräykseen.",
          "language": "fi"
        },
        {
          "value": "Sorteras som plast.",
          "language": "sv"
        }
      ],
      "usageInstructions": [],
      "classifications": [
        {
          "type": "DECIMAL",
          "name": "composition",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "gda",
          "values": [
            {
              "id": "CHOAVL",
              "value": 13.0,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 227.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 941.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 1.5,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 19.0,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 0.1,
              "unit": "GRM"
            },
            {
              "id": "LACS",
              "value": 0.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 1.4,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.55,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 2.7,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "mineral",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "nutritionFact",
          "values": [
            {
              "id": "CHOAVL",
              "value": 13.0,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 227.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 941.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 1.5,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 19.0,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 0.1,
              "unit": "GRM"
            },
            {
              "id": "LACS",
              "value": 0.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 1.4,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.55,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 2.7,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "vitamin",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packagingMarkedLabel",
          "values": [
            {
              "id": "GOODS_FROM_FINLAND_BLUE_SWAN",
              "synkkaId": "GOODS_FROM_FINLAND_BLUE_SWAN"
            },
            {
              "id": "coolTemperature"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "allergen",
          "values": [
            {
              "id": "AE",
              "unit": "CONTAINS"
            },
            {
              "id": "BM",
              "unit": "CONTAINS"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nonAllergen",
          "values": [
            {
              "id": "AC",
              "unit": "FREE_FROM"
            },
            {
              "id": "AF",
              "unit": "FREE_FROM"
            },
            {
              "id": "AM",
              "unit": "FREE_FROM"
            },
            {
              "id": "AN",
              "unit": "FREE_FROM"
            },
            {
              "id": "AP",
              "unit": "FREE_FROM"
            },
            {
              "id": "AS",
              "unit": "FREE_FROM"
            },
            {
              "id": "AU",
              "unit": "FREE_FROM"
            },
            {
              "id": "AW",
              "unit": "FREE_FROM"
            },
            {
              "id": "AY",
              "unit": "FREE_FROM"
            },
            {
              "id": "BC",
              "unit": "FREE_FROM"
            },
            {
              "id": "GB",
              "unit": "FREE_FROM"
            },
            {
              "id": "GO",
              "unit": "FREE_FROM"
            },
            {
              "id": "GS",
              "unit": "FREE_FROM"
            },
            {
              "id": "ML",
              "unit": "FREE_FROM"
            },
            {
              "id": "NL",
              "unit": "FREE_FROM"
            },
            {
              "id": "NR",
              "unit": "FREE_FROM"
            },
            {
              "id": "SA",
              "unit": "FREE_FROM"
            },
            {
              "id": "SC",
              "unit": "FREE_FROM"
            },
            {
              "id": "SH",
              "unit": "FREE_FROM"
            },
            {
              "id": "ST",
              "unit": "FREE_FROM"
            },
            {
              "id": "SW",
              "unit": "FREE_FROM"
            },
            {
              "id": "UM",
              "unit": "FREE_FROM"
            },
            {
              "id": "UW",
              "unit": "FREE_FROM"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nutritionalClaim",
          "values": [
            {
              "id": "FREE_FROM_GLUTEN",
              "synkkaId": "GLUTEN",
              "unit": "FREE_FROM"
            },
            {
              "id": "FREE_FROM_LACTOSE",
              "synkkaId": "LACTOSE",
              "unit": "FREE_FROM"
            },
            {
              "id": "VEGETARIAN",
              "synkkaId": "VEGETARIAN",
              "unit": "DIET"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "packaging",
          "values": []
        }
      ],
      "nutritionalContent": [
        {
          "id": "CHOAVL",
          "value": 13.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "ENER-E14",
          "value": 227.0,
          "unit": "E14",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "ENER-KJO",
          "value": 941.0,
          "unit": "KJO",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "FASAT",
          "value": 1.5,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "FAT",
          "value": 19.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "FIBTG",
          "value": 0.1,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "LACS",
          "value": 0.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "PRO-",
          "value": 1.4,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "SALTEQ",
          "value": 0.55,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        },
        {
          "id": "SUGAR-",
          "value": 2.7,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM",
          "servingSize": 100.0,
          "servingSizeUnit": "GRM"
        }
      ],
      "ingredients": [
        {
          "sequence": 1,
          "percentage": 56.0,
          "names": [
            {
              "value": "potato",
              "language": "en"
            },
            {
              "value": "Peruna",
              "language": "fi"
            },
            {
              "value": "potatis",
              "language": "sv"
            }
          ],
          "origins": [
            {
              "type": "FARMING",
              "country": "246"
            }
          ]
        }
      ],
      "medias": [
        {
          "id": 52633,
          "primary": true
        }
      ],
      "children": [],
      "fishingReports": [],
      "safetyData": [],
      "brand": "Forssan",
      "variableUnit": false,
      "vatCode": "MEDIUM",
      "producers": [
        {
          "id": "6407809999995",
          "name": "Atria Suomi Oy"
        }
      ],
      "unitConversions": [
        {
          "synkkaPackagingType": "BASE_UNIT_OR_EACH",
          "width": {
            "unit": "MMT",
            "value": 166.0
          },
          "length": {
            "unit": "MMT",
            "value": 50.0
          },
          "height": {
            "unit": "MMT",
            "value": 101.0
          },
          "volume": {
            "unit": "KGM",
            "value": 0.4
          },
          "netWeight": {
            "unit": "KGM",
            "value": 0.4
          },
          "grossWeight": {
            "unit": "GRM",
            "value": 423.0
          }
        }
      ],
      "minTemperature": 5.0,
      "maxTemperature": 8.0
    },
    "units": [
      {
        "unitId": "PAL",
        "gtin": "6409460046902",
        "sizeInBaseUnits": 50.0
      },
      {
        "unitId": "KI",
        "gtin": "6409460046896",
        "sizeInBaseUnits": 5.0
      },
      {
        "unitId": "RAS",
        "gtin": "6409460002724",
        "sizeInBaseUnits": 1.0
      }
    ],
    "deposits": [],
    "substitutions": NaN
  },
  {
    "salesUnitGtin": "6416597016579",
    "salesUnit": "SK",
    "baseUnit": "SK",
    "category": "21380",
    "allowedLotSize": 0.01,
    "deleted": false,
    "temperatureCondition": 8.0,
    "vendorName": "RAVINTORAISIO OY KUIVA",
    "countryOfOrigin": "fi",
    "synkkaData": {
      "gtin": "6416597016579",
      "lastUpdated": "2025-09-25T11:50:47+0300",
      "mediasLastUpdated": "2025-05-28T16:57:07+0300",
      "countriesOfOrigin": [
        "246"
      ],
      "names": [
        {
          "value": "Torino 10kg macaroni",
          "language": "en"
        },
        {
          "value": "Torino 10kg suurkeittiömakaroni",
          "language": "fi"
        },
        {
          "value": "Torino 10kg storköksmakaroni",
          "language": "sv"
        }
      ],
      "materialAdditionalDescriptions": [],
      "marketingTexts": [
        {
          "value": "Macaroni pasta for casseroles, salads and soups. Cooking time approx. 8 min. Weight 515 g/l. Use within 30 months.",
          "language": "en"
        },
        {
          "value": "Sarvimakaroni laatikkoruokien, salaattien ja keittojen valmistukseen. Kypsymisaika noin 8 min. Säilyvyys 30 kk.",
          "language": "fi"
        },
        {
          "value": "Böjda makaroner för tillagning av lådrätter, sallader och soppor. Tillagningstid cirka 8 min. Hållbarhet 30 månader.",
          "language": "sv"
        }
      ],
      "keyIngredients": [
        {
          "value": "WHEAT flour (Finland), water. May contain traces of oats, rye.",
          "language": "en"
        },
        {
          "value": "VEHNÄjauho (Suomi), vesi. Saattaa sisältää pieniä määriä kauraa, ruista.",
          "language": "fi"
        },
        {
          "value": "VETEmjöl (Finland), vatten. Kan innehålla spår av havre, råg.",
          "language": "sv"
        }
      ],
      "storageInstructions": [
        {
          "value": "In a cool and dry place.",
          "language": "en"
        },
        {
          "value": "Kuivassa ja viileässä.",
          "language": "fi"
        },
        {
          "value": "Torrt och svalt.",
          "language": "sv"
        }
      ],
      "preparationInstructions": [
        {
          "value": "Torino macaroni withstands various production processes (cook&serve, cook&chill and cold preparation) and heat holding well.",
          "language": "en"
        },
        {
          "value": "Torino suurkeittiömakaroni kestää hyvin eri tuotantoprosessit (cook&serve, cook&chill ja kylmävalmistus) ja lämpösäilytyksen.",
          "language": "fi"
        },
        {
          "value": "Torino storköksmakaroni tål olika produktionsprocesser (cook&serve, cook&chill och kallberedning) samt varmhållning bra.",
          "language": "sv"
        }
      ],
      "disposalInformations": [
        {
          "value": "Empty package is sorted for carton recycling.",
          "language": "en"
        },
        {
          "value": "Tyhjä pakkaus lajitellaan kartonkikeräykseen.",
          "language": "fi"
        },
        {
          "value": "Den tomma förpackningen kan sorteras som kartong.",
          "language": "sv"
        }
      ],
      "usageInstructions": [],
      "classifications": [
        {
          "type": "DECIMAL",
          "name": "composition",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "gda",
          "values": [
            {
              "id": "CHOAVL",
              "value": 68.0,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 359.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 1501.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 0.5,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 2.5,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 4.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 13.0,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.0,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 1.3,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "mineral",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "nutritionFact",
          "values": [
            {
              "id": "CHOAVL",
              "value": 68.0,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 359.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 1501.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 0.5,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 2.5,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 4.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 13.0,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.0,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 1.3,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "vitamin",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packagingMarkedLabel",
          "values": [
            {
              "id": "GOODS_FROM_FINLAND_BLUE_SWAN",
              "synkkaId": "GOODS_FROM_FINLAND_BLUE_SWAN"
            },
            {
              "id": "warmTemperature"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "allergen",
          "values": [
            {
              "id": "AW",
              "unit": "CONTAINS"
            },
            {
              "id": "GO",
              "unit": "MAY_CONTAIN"
            },
            {
              "id": "NR",
              "unit": "MAY_CONTAIN"
            },
            {
              "id": "UW",
              "unit": "CONTAINS"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nonAllergen",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "nutritionalClaim",
          "values": [
            {
              "id": "VEGAN",
              "synkkaId": "VEGAN",
              "unit": "DIET"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "packaging",
          "values": []
        }
      ],
      "nutritionalContent": [
        {
          "id": "CHOAVL",
          "value": 68.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "ENER-E14",
          "value": 359.0,
          "unit": "E14",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "ENER-KJO",
          "value": 1501.0,
          "unit": "KJO",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "FASAT",
          "value": 0.5,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "FAT",
          "value": 2.5,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "FIBTG",
          "value": 4.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "PRO-",
          "value": 13.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "SALTEQ",
          "value": 0.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "SUGAR-",
          "value": 1.3,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        }
      ],
      "ingredients": [],
      "medias": [
        {
          "id": 94328,
          "primary": true
        }
      ],
      "children": [],
      "fishingReports": [],
      "safetyData": [],
      "brand": "Torino",
      "variableUnit": false,
      "vatCode": "MEDIUM",
      "producers": [
        {
          "id": "6411209999998",
          "name": "RavintoRaisio Oy"
        }
      ],
      "unitConversions": [
        {
          "synkkaPackagingType": "BASE_UNIT_OR_EACH",
          "width": {
            "unit": "MMT",
            "value": 330.0
          },
          "length": {
            "unit": "MMT",
            "value": 120.0
          },
          "height": {
            "unit": "MMT",
            "value": 490.0
          },
          "volume": {
            "unit": "GRM",
            "value": 10000.0
          },
          "netWeight": {
            "unit": "GRM",
            "value": 10000.0
          },
          "grossWeight": {
            "unit": "GRM",
            "value": 10095.0
          }
        }
      ],
      "minTemperature": 2.0,
      "maxTemperature": 25.0
    },
    "units": [
      {
        "unitId": "SK",
        "gtin": "6416597016579",
        "sizeInBaseUnits": 1.0
      },
      {
        "unitId": "PAL",
        "sizeInBaseUnits": 49.0
      }
    ],
    "deposits": [],
    "substitutions": NaN
  },
  {
    "salesUnitGtin": "6416796729140",
    "salesUnit": "ST",
    "baseUnit": "ST",
    "category": "21904",
    "allowedLotSize": 0.01,
    "deleted": false,
    "temperatureCondition": 8.0,
    "vendorName": "PULJONKI OY PULJONKI",
    "countryOfOrigin": "fi",
    "synkkaData": {
      "gtin": "6416796729140",
      "lastUpdated": "2025-09-19T12:07:38+0300",
      "mediasLastUpdated": "2025-09-08T09:53:23+0300",
      "countriesOfOrigin": [
        "246"
      ],
      "names": [
        {
          "value": "Puljonki® Plum Tomato Sauce 1 l tetra",
          "language": "en"
        },
        {
          "value": "Puljonki® Luumutomaattikastike 1 l tetra",
          "language": "fi"
        },
        {
          "value": "Puljonki® Plommontomatsås 1 l tetra",
          "language": "sv"
        }
      ],
      "materialAdditionalDescriptions": [],
      "marketingTexts": [
        {
          "value": "Plum tomato sauce made in the traditional Italian way. Clear, clean and fresh tomato flavour, complemented by basil, cayenne pepper and chilli. Excellent pizza sauce and tomato soup base. Serve Italian style with meatballs and pasta.",
          "language": "en"
        },
        {
          "value": "Puljonki® Luumutomaattikastike on perinteiseen italialaiseen tapaan valmistettu luumutomaattikastike. Selkeä, puhdas ja raikas tomaattinen maku, jota täydennetään basilikalla, cayennepippurilla sekä chilillä. Erinomainen pizzakastike ja tomaattikeiton pohja. Tarjoile italialaisittain lihapullien ja pastan kera.\n1 litra, käyttövalmis.",
          "language": "fi"
        },
        {
          "value": "Plommontomatsås gjord på traditionellt italienskt sätt. Klar, ren och fräsch tomatsmak, kompletterad med basilika, cayennepeppar och chili. Utmärkt pizzasås och tomatsoppabotten. Servera italiensk stil med köttbullar och pasta.",
          "language": "sv"
        }
      ],
      "keyIngredients": [
        {
          "value": "Tomato 51% (crushed tomato, tomato purée), water, sugar, olive oil, modified starch, salt, basil, garlic, red wine vinegar, thyme, parsley, cayenne pepper.",
          "language": "en"
        },
        {
          "value": "Tomaatti 51% (tomaattimurska, tomaattipyre), vesi, sokeri, oliiviöljy, muunnettu tärkkelys, suola, basilika, valkosipuli, punaviinietikka, timjami, persilja, cayennepippuri.",
          "language": "fi"
        },
        {
          "value": "Tomat 51% (krossade tomat, tomatpuree), vatten, socker, olivolja, modifierad stärkelse, salt, basilika, vitlök, rödvinsvinäger, timjan, persilja, cayennepeppa.",
          "language": "sv"
        }
      ],
      "storageInstructions": [
        {
          "value": "Storage: Unopened at room temperature. Once opened, 3 days at max. +5°C.",
          "language": "en"
        },
        {
          "value": "Säilytys: Säilyy avaamattomana huoneenlämmössä. Avattuna +5 °C, 3 päivää.",
          "language": "fi"
        },
        {
          "value": "Förvaring: Förvaras oöppnad i rumstemperatur. Öppnad i +5 °C, 3 dagar.",
          "language": "sv"
        }
      ],
      "preparationInstructions": [
        {
          "value": "Ready to use.",
          "language": "en"
        },
        {
          "value": "Käyttövalmis.",
          "language": "fi"
        },
        {
          "value": "Färdig at använda.",
          "language": "sv"
        }
      ],
      "disposalInformations": [
        {
          "value": "Recycle packaging as cardboard.",
          "language": "en"
        },
        {
          "value": "Kierrätä pakkaus kartonkikeräykseen.",
          "language": "fi"
        },
        {
          "value": "Förpackningen sorteras som kartong.",
          "language": "sv"
        }
      ],
      "usageInstructions": [
        {
          "value": "Ready to use.",
          "language": "en"
        },
        {
          "value": "Käyttövalmis.",
          "language": "fi"
        },
        {
          "value": "Färdig at använda.",
          "language": "sv"
        }
      ],
      "classifications": [
        {
          "type": "DECIMAL",
          "name": "composition",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "gda",
          "values": [
            {
              "id": "CHOAVL",
              "value": 9.3,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 54.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 227.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 0.1,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 1.0,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 1.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 1.5,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.77,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 7.7,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "mineral",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "nutritionFact",
          "values": [
            {
              "id": "CHOAVL",
              "value": 9.3,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 54.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 227.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 0.1,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 1.0,
              "unit": "GRM"
            },
            {
              "id": "FIBTG",
              "value": 1.0,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 1.5,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 0.77,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 7.7,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "vitamin",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packagingMarkedLabel",
          "values": [
            {
              "id": "warmTemperature"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "allergen",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "nonAllergen",
          "values": [
            {
              "id": "AC",
              "unit": "FREE_FROM"
            },
            {
              "id": "AE",
              "unit": "FREE_FROM"
            },
            {
              "id": "AF",
              "unit": "FREE_FROM"
            },
            {
              "id": "AM",
              "unit": "FREE_FROM"
            },
            {
              "id": "AN",
              "unit": "FREE_FROM"
            },
            {
              "id": "AP",
              "unit": "FREE_FROM"
            },
            {
              "id": "AS",
              "unit": "FREE_FROM"
            },
            {
              "id": "AU",
              "unit": "FREE_FROM"
            },
            {
              "id": "AW",
              "unit": "FREE_FROM"
            },
            {
              "id": "AY",
              "unit": "FREE_FROM"
            },
            {
              "id": "BC",
              "unit": "FREE_FROM"
            },
            {
              "id": "BM",
              "unit": "FREE_FROM"
            },
            {
              "id": "ML",
              "unit": "FREE_FROM"
            },
            {
              "id": "NL",
              "unit": "FREE_FROM"
            },
            {
              "id": "UM",
              "unit": "FREE_FROM"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nutritionalClaim",
          "values": [
            {
              "id": "FREE_FROM_GLUTEN",
              "synkkaId": "GLUTEN",
              "unit": "FREE_FROM"
            },
            {
              "id": "FREE_FROM_LACTOSE",
              "synkkaId": "LACTOSE",
              "unit": "FREE_FROM"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "packaging",
          "values": []
        }
      ],
      "nutritionalContent": [
        {
          "id": "CHOAVL",
          "value": 9.3,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "ENER-E14",
          "value": 54.0,
          "unit": "E14",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "ENER-KJO",
          "value": 227.0,
          "unit": "KJO",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "FASAT",
          "value": 0.1,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "FAT",
          "value": 1.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "FIBTG",
          "value": 1.0,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "PRO-",
          "value": 1.5,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "SALTEQ",
          "value": 0.77,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        },
        {
          "id": "SUGAR-",
          "value": 7.7,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "MLT",
          "servingSize": 100.0,
          "servingSizeUnit": "MLT"
        }
      ],
      "ingredients": [],
      "medias": [
        {
          "id": 3691839,
          "primary": true
        },
        {
          "id": 3691840,
          "primary": false
        },
        {
          "id": 64167967291401,
          "primary": true
        },
        {
          "id": 64167967291402,
          "primary": false
        }
      ],
      "children": [],
      "fishingReports": [],
      "safetyData": [],
      "brand": "Puljonki®",
      "variableUnit": false,
      "vatCode": "MEDIUM",
      "producers": [
        {
          "id": "5790001394523",
          "name": "OSCAR A/S"
        }
      ],
      "unitConversions": [
        {
          "synkkaPackagingType": "BASE_UNIT_OR_EACH",
          "width": {
            "unit": "MMT",
            "value": 73.0
          },
          "length": {
            "unit": "MMT",
            "value": 72.0
          },
          "height": {
            "unit": "MMT",
            "value": 199.0
          },
          "volume": {
            "unit": "LTR",
            "value": 1.0
          },
          "netWeight": {
            "unit": "GRM",
            "value": 1043.0
          },
          "grossWeight": {
            "unit": "GRM",
            "value": 1075.0
          }
        }
      ],
      "minTemperature": 5.0,
      "maxTemperature": 20.0
    },
    "units": [
      {
        "unitId": "KI",
        "gtin": "6416796809798",
        "sizeInBaseUnits": 6.0
      },
      {
        "unitId": "ST",
        "gtin": "6416796729140",
        "sizeInBaseUnits": 1.0
      }
    ],
    "deposits": [],
    "substitutions": NaN
  },
  {
    "salesUnitGtin": "5017764112264",
    "salesUnit": "KI",
    "baseUnit": "BAG",
    "category": "21990",
    "allowedLotSize": 0.01,
    "deleted": false,
    "temperatureCondition": 8.0,
    "vendorName": "LEJOS OY",
    "countryOfOrigin": "gb",
    "synkkaData": {
      "gtin": "5017764112257",
      "lastUpdated": "2025-05-28T17:24:59+0300",
      "mediasLastUpdated": "2025-05-28T17:24:59+0300",
      "countriesOfOrigin": [
        "528"
      ],
      "names": [
        {
          "value": "40g Kettle Chips Sea Salt & Balsamic Vinegar Potato Chips",
          "language": "en"
        },
        {
          "value": "40g Kettle Chips Sea Salt & Balsamic Vinegar Perunalastut",
          "language": "fi"
        },
        {
          "value": "40g Kettle Chips Sea Salt & Balsamic Vinegar Potatischips",
          "language": "sv"
        }
      ],
      "materialAdditionalDescriptions": [],
      "marketingTexts": [
        {
          "value": "Kettle's high-quality potato chips also in a small 40g bag. More than 10 years ago Kettle's head chef Chris hit upon the idea of complementing sea salt with real balsamic vinegar. Modena balsamic vinegar creates a perfect balance and taste to potato chips. ",
          "language": "en"
        },
        {
          "value": "Kettlen laadukkaat perunalastut myös pienessä 40g pussissa. Yli 10 vuotta sitten Kettlen pääkokki Chris sai idean lisätä merisuolalla maustettuihin sipseihin hieman balsamiviinietikkaa.\nModena-balsamiviinietikka luo perunalastuihin täydellisen tasapainoisen maun.",
          "language": "fi"
        },
        {
          "value": "Kettles kvalitativa potatischips även i en liten 40g påse. För mer än 10 år sedan fick Kettles huvudkock Chris idén att lägga till lite balsamvinäger till chipsen som är kryddade med havssalt. Modena-balsamvinäger skapar en perfekt balans och smak i potatischipsen.",
          "language": "sv"
        }
      ],
      "keyIngredients": [
        {
          "value": "Potatoes, sunflower oil, sea salt, balsamic vinegar of Modena \"aceto balsamico di Modena igp\", potato maltodextrin, sugar, potato starch, acid: citric acid; natural flavouring.",
          "language": "en"
        },
        {
          "value": "Peruna, auringonkukkaöljy, merisuola, Modenan Balsamiviinietikka \"aceto balsamico di Modena igp\", maltodekstriini (peruna), sokeri, perunatärkkelys, happo: sitruunahappo, kuivattu punaviiniuute, luontainen aromi.",
          "language": "fi"
        },
        {
          "value": "Potatis, solrosolja, havssalt, balsamvinäger av modena, potatismaltodextrin, socker, potatistärkelse, syra: citronsyra; naturlig arom.",
          "language": "sv"
        }
      ],
      "storageInstructions": [
        {
          "value": "Store in a cool, dry place.",
          "language": "en"
        },
        {
          "value": "Säilyts viileässä, kuivassa paikassa.",
          "language": "fi"
        },
        {
          "value": "Förvaras svalt och torrt.",
          "language": "sv"
        }
      ],
      "preparationInstructions": [],
      "disposalInformations": [],
      "usageInstructions": [],
      "classifications": [
        {
          "type": "DECIMAL",
          "name": "composition",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "gda",
          "values": [
            {
              "id": "CHOAVL",
              "value": 56.8,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 513.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 2142.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 2.4,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 28.9,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 4.3,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 1.6,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 1.3,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "mineral",
          "values": []
        },
        {
          "type": "DECIMAL",
          "name": "nutritionFact",
          "values": [
            {
              "id": "CHOAVL",
              "value": 56.8,
              "unit": "GRM"
            },
            {
              "id": "ENER-E14",
              "value": 513.0,
              "unit": "E14"
            },
            {
              "id": "ENER-KJO",
              "value": 2142.0,
              "unit": "KJO"
            },
            {
              "id": "FASAT",
              "value": 2.4,
              "unit": "GRM"
            },
            {
              "id": "FAT",
              "value": 28.9,
              "unit": "GRM"
            },
            {
              "id": "PRO-",
              "value": 4.3,
              "unit": "GRM"
            },
            {
              "id": "SALTEQ",
              "value": 1.6,
              "unit": "GRM"
            },
            {
              "id": "SUGAR-",
              "value": 1.3,
              "unit": "GRM"
            }
          ]
        },
        {
          "type": "DECIMAL",
          "name": "vitamin",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packagingMarkedLabel",
          "values": [
            {
              "id": "warmTemperature"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "allergen",
          "values": [
            {
              "id": "X99",
              "unit": "CONTAINS"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nonAllergen",
          "values": [
            {
              "id": "AC",
              "unit": "FREE_FROM"
            },
            {
              "id": "AE",
              "unit": "FREE_FROM"
            },
            {
              "id": "AF",
              "unit": "FREE_FROM"
            },
            {
              "id": "AM",
              "unit": "FREE_FROM"
            },
            {
              "id": "AN",
              "unit": "FREE_FROM"
            },
            {
              "id": "AP",
              "unit": "FREE_FROM"
            },
            {
              "id": "AS",
              "unit": "FREE_FROM"
            },
            {
              "id": "AU",
              "unit": "FREE_FROM"
            },
            {
              "id": "AW",
              "unit": "FREE_FROM"
            },
            {
              "id": "AY",
              "unit": "FREE_FROM"
            },
            {
              "id": "BC",
              "unit": "FREE_FROM"
            },
            {
              "id": "BM",
              "unit": "FREE_FROM"
            },
            {
              "id": "NL",
              "unit": "FREE_FROM"
            },
            {
              "id": "UM",
              "unit": "FREE_FROM"
            }
          ]
        },
        {
          "type": "ENUM",
          "name": "nutritionalClaim",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packaging",
          "values": []
        }
      ],
      "nutritionalContent": [
        {
          "id": "CHOAVL",
          "value": 56.8,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "ENER-E14",
          "value": 513.0,
          "unit": "E14",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "ENER-KJO",
          "value": 2142.0,
          "unit": "KJO",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "FASAT",
          "value": 2.4,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "FAT",
          "value": 28.9,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "PRO-",
          "value": 4.3,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "SALTEQ",
          "value": 1.6,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        },
        {
          "id": "SUGAR-",
          "value": 1.3,
          "unit": "GRM",
          "unitPrecision": "APPROXIMATELY",
          "basisQuantity": 100.0,
          "basisQuantityUnit": "GRM"
        }
      ],
      "ingredients": [],
      "medias": [
        {
          "id": 85750,
          "primary": true
        },
        {
          "id": 3234087,
          "primary": true
        }
      ],
      "children": [],
      "fishingReports": [],
      "safetyData": [],
      "brand": "Kettle",
      "variableUnit": false,
      "vatCode": "MEDIUM",
      "producers": [
        {
          "id": "6429901107702",
          "name": "Lejos Oy"
        }
      ],
      "unitConversions": [
        {
          "synkkaPackagingType": "CASE",
          "width": {
            "unit": "MMT",
            "value": 293.0
          },
          "length": {
            "unit": "MMT",
            "value": 388.0
          },
          "height": {
            "unit": "MMT",
            "value": 167.0
          },
          "netWeight": {
            "unit": "GRM",
            "value": 720.0
          },
          "grossWeight": {
            "unit": "GRM",
            "value": 1028.0
          }
        }
      ],
      "minTemperature": 5.0,
      "maxTemperature": 25.0
    },
    "units": [
      {
        "unitId": "BAG",
        "gtin": "5017764112257",
        "sizeInBaseUnits": 1.0
      },
      {
        "unitId": "KI",
        "gtin": "5017764112264",
        "sizeInBaseUnits": 18.0
      }
    ],
    "deposits": [],
    "substitutions": NaN
  },
  {
    "salesUnitGtin": "8714521950172",
    "salesUnit": "ST",
    "baseUnit": "ST",
    "category": "17401",
    "allowedLotSize": 0.01,
    "deleted": false,
    "temperatureCondition": 5.0,
    "vendorName": "BUD HOLLAND B.V.",
    "countryOfOrigin": "nl",
    "synkkaData": {
      "names": [
        {
          "value": "TOMBERRY 125G",
          "language": "en"
        },
        {
          "value": "TOMAATTI \"TOM BERRY\" 125G RASIA HOLLANT",
          "language": "fi"
        },
        {
          "value": "TOMBERRY 125G",
          "language": "sv"
        }
      ],
      "materialAdditionalDescriptions": [],
      "marketingTexts": [],
      "keyIngredients": [],
      "classifications": [
        {
          "type": "ENUM",
          "name": "packagingMarkedLabel",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "allergen",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "nonAllergen",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "nutritionalClaim",
          "values": []
        },
        {
          "type": "ENUM",
          "name": "packaging",
          "values": []
        }
      ],
      "nutritionalContent": [],
      "medias": []
    },
    "units": [
      {
        "unitId": "KI",
        "sizeInBaseUnits": 8.0
      },
      {
        "unitId": "ST",
        "gtin": "8714521950172",
        "sizeInBaseUnits": 1.0
      }
    ],
    "deposits": [],
    "substitutions": NaN
  }
]
```