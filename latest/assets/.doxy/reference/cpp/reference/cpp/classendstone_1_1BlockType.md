

# Class endstone::BlockType



[**ClassList**](annotated.md) **>** [**endstone**](namespaceendstone.md) **>** [**BlockType**](classendstone_1_1BlockType.md)




























## Public Static Attributes

| Type | Name |
| ---: | :--- |
|  [**constexpr**](classendstone_1_1Identifier.md) [**auto**](classendstone_1_1Identifier.md) | [**Air**](#variable-air)   = `BlockTypeId::minecraft("air")`<br> |














## Public Functions

| Type | Name |
| ---: | :--- |
| virtual std::unique\_ptr&lt; [**BlockData**](classendstone_1_1BlockData.md) &gt; | [**createBlockData**](#function-createblockdata) () const = 0<br>_Creates a new_ [_**BlockData**_](classendstone_1_1BlockData.md) _instance for this block type, with all properties initialized to unspecified defaults._ |
| virtual [**BlockTypeId**](classendstone_1_1Identifier.md) | [**getId**](#function-getid) () const = 0<br>_Return the identifier of this block type._  |
| virtual std::string | [**getTranslationKey**](#function-gettranslationkey) () const = 0<br>_Get the translation key, suitable for use in a translation component._  |
| virtual [**bool**](classendstone_1_1Identifier.md) | [**hasItemType**](#function-hasitemtype) () const = 0<br>_Returns true if this_ [_**BlockType**_](classendstone_1_1BlockType.md) _has a corresponding_[_**ItemType**_](classendstone_1_1ItemType.md) _._ |
|   | [**operator BlockTypeId**](#function-operator-blocktypeid) () const<br> |
|  [**bool**](classendstone_1_1Identifier.md) | [**operator!=**](#function-operator) ([**const**](classendstone_1_1Identifier.md) [**BlockTypeId**](classendstone_1_1Identifier.md) & other) const<br> |
|  [**bool**](classendstone_1_1Identifier.md) | [**operator!=**](#function-operator_1) ([**const**](classendstone_1_1Identifier.md) [**BlockType**](classendstone_1_1BlockType.md) & other) const<br> |
|  [**bool**](classendstone_1_1Identifier.md) | [**operator==**](#function-operator_2) ([**const**](classendstone_1_1Identifier.md) [**BlockTypeId**](classendstone_1_1Identifier.md) & other) const<br> |
|  [**bool**](classendstone_1_1Identifier.md) | [**operator==**](#function-operator_3) ([**const**](classendstone_1_1Identifier.md) [**BlockType**](classendstone_1_1BlockType.md) & other) const<br> |
| virtual  | [**~BlockType**](#function-blocktype) () = default<br> |




























## Public Static Attributes Documentation




### variable Air 

```C++
constexpr auto endstone::BlockType::Air;
```




<hr>
## Public Functions Documentation




### function createBlockData 

_Creates a new_ [_**BlockData**_](classendstone_1_1BlockData.md) _instance for this block type, with all properties initialized to unspecified defaults._
```C++
virtual std::unique_ptr< BlockData > endstone::BlockType::createBlockData () const = 0
```





**Returns:**

new data instance 





        

<hr>



### function getId 

_Return the identifier of this block type._ 
```C++
virtual BlockTypeId endstone::BlockType::getId () const = 0
```





**Returns:**

this block type's identifier 





        

<hr>



### function getTranslationKey 

_Get the translation key, suitable for use in a translation component._ 
```C++
virtual std::string endstone::BlockType::getTranslationKey () const = 0
```





**Returns:**

the translation key 





        

<hr>



### function hasItemType 

_Returns true if this_ [_**BlockType**_](classendstone_1_1BlockType.md) _has a corresponding_[_**ItemType**_](classendstone_1_1ItemType.md) _._
```C++
virtual bool endstone::BlockType::hasItemType () const = 0
```





**Returns:**

true if there is a corresponding [**ItemType**](classendstone_1_1ItemType.md), otherwise false 





        

<hr>



### function operator BlockTypeId 

```C++
inline endstone::BlockType::operator BlockTypeId () const
```




<hr>



### function operator!= 

```C++
inline bool endstone::BlockType::operator!= (
    const  BlockTypeId & other
) const
```




<hr>



### function operator!= 

```C++
inline bool endstone::BlockType::operator!= (
    const  BlockType & other
) const
```




<hr>



### function operator== 

```C++
inline bool endstone::BlockType::operator== (
    const  BlockTypeId & other
) const
```




<hr>



### function operator== 

```C++
inline bool endstone::BlockType::operator== (
    const  BlockType & other
) const
```




<hr>



### function ~BlockType 

```C++
virtual endstone::BlockType::~BlockType () = default
```




<hr>

------------------------------
The documentation for this class was generated from the following file `include/endstone/block/block_type.h`

