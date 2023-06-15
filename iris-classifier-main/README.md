# iris-classification

class Sample

class Purpose
-코드에서 사용할수있는 세가지 객체인 purpose.classification, purpose.testing, purpose.traning 이 있는 네임스페이스를 만든다.

class KnownSample
-from_dict 메서드는 종 값을 확인하여 유효하지 않은 경우 예외를 발생시킨다. @classmethod 데코레이터와 함께 정의된다. 이것은 실제 클래스 객체가 첫번째 매개변수인 cls 가 됨을 의미한다. 
-@property메서드는 속성이름으로 표시될 메서드를 정의한다.

class UnknownSample

class TrainingKnownSample
- from_dict() 가 실제로 사용되는 위치에 cast()작업을 두는 것이다.

class TrainingData
- TrainingData가 다양한 Hyperparameter 에 대한 시도를 기록하기에 적합한 장소이다. 그러므로 가장높은 정확도로 아이리스를 분류하는 k값을 갖는 Hyperparameter 인스턴스를 식별할 수 있다.
-training, testing, tuning 속성은 sample 객체와 hyperparameter 객체를 가진다. 
-load 메서드는 다른 객체에서 제공받은 데이터를 처리하도록 디자인 되어있다.
샘플을 테스트 및 학습 하위 집합으로 분할한다. InvalidSampleError 오류를 포착해 메시지를 표시하고 문제의 발생횟수를 센다.
-test와 classify 메서드는 대부분의 작업을 Hyperparameter 클래스에 위임한다.

class ED
-맨해튼 거리 계산에서 변형을 수행하는 Distnce의 하위클래스.
거리계산에서 제곱 및 제곱근을 실행하기 위해 math.hypot() 함수를 활용했다.

class MD
- 체비쇼프의 거리 계산에서 변형을 수행하는 Distnce의 하위클래스.
- 체비쇼프의 거리는 서로 더 가까이에 있는 이웃을 강조하는 경향이 있다.

class SD
- distace의 새하위 클래스를 추가해 맨해튼 거리와 쇠렌센 거리 계산을 디자인에 도입하였다.
- 객체지향적 상속을 활용해 거리 계산 함수의 다형성 패밀리를 구축할 수 있게 해준다.

class InvalidSampleError
- 애플리케이션이 처리할 수 없는 입력 데이터에 대해 InvalidSampleError 예외를 발생시킬 수 있다.
-ValueError 예외를 발생시킬수 있는 코드 상의 버그와 InvalidSampleError 예외를 발생시킬수 있는 잘못된 데이터가 있는 경우를 구별하는데 도움된다.

class OutlierError
-단순한 범위 확인 또는 이상치 탐지를 위한 mad 방법과 함께 사용할 수 있다.