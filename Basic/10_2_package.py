#travel
#클래스, 함수는 import로 직접 호출 할 수 없으니 주의. from을 이용하면 가져올 수 있음.

import for_package_10_2.for_package_10_2_2
trip_to1 = for_package_10_2.for_package_10_2_2.VietnamPackage()
trip_to1.detail()

from for_package_10_2 import for_package_10_2_2
trip_to2 = for_package_10_2_2.VietnamPackage()
trip_to2.detail()

from for_package_10_2.for_package_10_2_2 import VietnamPackage
trip_to3 = VietnamPackage()
trip_to3.detail()

from for_package_10_2 import for_package_10_2_1
trip_to4 = for_package_10_2_1.ThailandPackage()
trip_to4.detail()