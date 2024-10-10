## Design Pattern With Python
디자인 패턴은 개발하면서 발생하는 반복적인 문제들을 어떻게 해결할 것인지에 대한 해결 방안으로 객체 지향 프로그래밍 설계를 할 때 자주 발생하는 문제들을 피하기 위해 사용되는 패턴.     
이러한 디자인 패턴은 객체 지향 4대 특성(`캡슐화`, `상속`, `추상화`, `다형성`)과 설계 원칙(`SOLID`)을 기반으로 구현되어 있다. 

</br>

### 객체 지향 다섯 가지 설계 원칙

1. `단일 책임 원칙` (**S**ingle Responsibility Principle)
   - 각 클래스는 하나의 기능 또는 책임만을 가짐 -> 코드의 복잡성을 줄이고, 유지보수를 용이하게 함.
2. `개방-폐쇄 원칙` (**O**pen-Closed Principle)
   - 소프트웨어 엔티티는 확장에는 열려 있어야 하지만, 수정에는 닫혀 있어야 한다.
   - 기존 코드를 변경하지 않고도 시스템의 기능을 확장할 수 있도록 함.
3. `리스코프 치환 원칙` (**L**iskov Substitution Principle)
    - 파생 클래스는 기반 클래스의 기능을 손상시키지 않으면서 대체 가능해야 한다. 
4. `인터페이스 분리 원칙` (**I**nterface Segregation Principle)
   - 클라이언트는 사용하지 않는 메소드에 의존하도록 강제되면 안됨 -> 더 작고 구체적인 인터페이스로 분리 
5. `의존성 역전 원칙` (**D**ependency Inversion Principle)
   - 고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화에 의존해야 한다. 

</br>

### 디자인 패턴의 장점

- **재사용성** : 반복적인 문제에 대한 일반적인 해결책을 제공하므로, 이를 재사용하여 유사한 상황에서 코드를 더 쉽게 작성할 수 있다.
- **가독성** : 일정한 구조로 정리하고 명확하게 작성하여 개발자가 코드를 이해하고 유지보수하기 쉽게 만든다.
- **유지보수성** : 코드를 쉽게 모듈화 할 수 있으며, 변경이 필요한 경우 해당 모듈만 수정하여 유지보수가 쉬워진다.
- **확장성** : 새로운 기능을 추가하거나 변경할 때 디자인 패턴을 활용하여 기존 코드를 변경하지 않고도 새로운 기능을 통합할 수 있다.
- **안정성과 신뢰성** : 수많은 사람들이 인정한 모범 사례로 검증된 솔루션을 제공한다.

</br>

### 생성 패턴(Creational Pattern)
****
객체 인스턴스를 생성하는 패턴으로, 클라이언트와 그 클라이언트가 생성해야 하는 객체 인스턴스 사이의 연결을 끊어 주는 패턴

|name|description|
|-|-|
|[빌더 패턴(builder pattern)](https://github.com/fore0919/design-pattern/blob/main/Creational/Builder.ipynb)|복잡한 객체의 생성 과정을 단순화하고, 객체를 단계적으로 생성하며 구성하는 패턴|
|[추상 팩토리(abstract pattern)](https://github.com/fore0919/design-pattern/blob/main/Creational/Abstract%20Factory.ipynb)|인터페이스를 정의하여 객체 생성을 추상화한 팩토리|


</br>


### 구조 패턴(Structural Pattern)
****
클래스와 객체를 더 큰 구조로 만들 수 있게 구상을 사용하는 패턴
|name|description|
|-|-|
|[데코레이터 패턴(decorator pattern)](https://github.com/fore0919/design-pattern/blob/main/Structural/Decorator.ipynb)|객체에 추가적인 기능을 동적으로 더할 수 있게 해주는 패턴|
|[퍼사드 패턴(facade pattern)](https://github.com/fore0919/design-pattern/blob/main/Structural/Facade.ipynb)|간단한 인터페이스를 제공하여 서브시스템의 복잡성을 숨기고, 클라이언트와 서브시스템 간의 상호작용을 간소화|
|[저장소 패턴(repository pattern)](https://github.com/fore0919/design-pattern/blob/main/Structural/Repository.ipynb)|데이터 저장소의 독립성을 보장하고 비즈니스 로직을 데이터 액세스 코드로부터 분리하는 디자인 패턴|

</br>

### 행위 패턴(Behavioral Pattern)
****
클래스와 객체들이 상호작용하는 방법과 역할을 분담하는 방법을 다루는 패턴

</br>
